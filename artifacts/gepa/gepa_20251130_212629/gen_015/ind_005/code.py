
import pretty_midi

# Initialize the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
instrument = pretty_midi.Instrument(program=64)  # Tenor Sax
midi.instruments.append(instrument)

# Time signature: 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes.append(time_signature)

# Key signature: F minor (no sharps/flats for now)
# We'll use F minor scale in the melody and chords

# Constants
BPM = 160
BEAT = 60.0 / BPM  # seconds per beat
BAR = 4 * BEAT  # seconds per bar
TOTAL_DURATION = 4 * BAR  # 4 bars

#---------------------
# Bar 1: Little Ray alone (drums)
#---------------------

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0, end=BEAT)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=2 * BEAT, end=3 * BEAT)
instrument.notes.extend([kick1, kick2])

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=1 * BEAT, end=1.5 * BEAT)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=3 * BEAT, end=3.5 * BEAT)
instrument.notes.extend([snare1, snare2])

# Hihat on every eighth
for i in range(8):
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=i * BEAT / 2, end=i * BEAT / 2 + 0.1875)
    instrument.notes.append(hihat)

#---------------------
# Bar 2: Diane on piano, comping on 2 and 4
#---------------------

# Diane plays 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
diane = pretty_midi.Instrument(program=0)  # Piano
midi.instruments.append(diane)

# Bar 2:
# Comp on beat 2 and 4 with Fm7 chords
# Beat 2: Fm7
for note in [53, 51, 55, 50]:  # F, Ab, C, Eb
    note_duration = 0.5 * BEAT
    note_start = 1 * BEAT
    note_end = note_start + note_duration
    diane_note = pretty_midi.Note(velocity=100, pitch=note, start=note_start, end=note_end)
    diane.notes.append(diane_note)

# Beat 4: Fm7 again, but with a slight syncopation
for note in [53, 51, 55, 50]:
    note_duration = 0.5 * BEAT
    note_start = 3 * BEAT
    note_end = note_start + note_duration
    diane_note = pretty_midi.Note(velocity=100, pitch=note, start=note_start, end=note_end)
    diane.notes.append(diane_note)

#---------------------
# Bar 3: Marcus on bass, walking line
#---------------------

# Marcus: Chromatic walking line, Fm bass line starting on Ab (Fm is F Ab Bb C Eb)
# Walking line: Ab -> Bb -> C -> Eb -> F -> Gb -> Ab -> Bb
# In quarter notes
bass = pretty_midi.Instrument(program=33)  # Bass
midi.instruments.append(bass)

notes = [79, 80, 82, 85, 53, 54, 79, 80]  # Ab, Bb, C, Eb, F, Gb, Ab, Bb
for i, note in enumerate(notes):
    start = i * BEAT
    end = start + BEAT
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

#---------------------
# Bar 4: Dante on tenor sax, motif with space and tension
#---------------------

# Tenor sax: short motif, space, tension, question
# Fm7 scale: F, Ab, Bb, C, Eb, F, Gb, Ab

# Soprano voice: F, then Ab, then a space, then a Gb (a quarter note after the Ab)
tenor_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=0, end=0.5 * BEAT),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=0.5 * BEAT, end=1 * BEAT),  # Ab
]

# Add a rest (silence) for half a beat
# Then a Gb (Fm7 scale) on beat 1.5
tenor_notes.append(pretty_midi.Note(velocity=110, pitch=54, start=1.5 * BEAT, end=2 * BEAT))  # Gb

# End of the motif — doesn't resolve, lingers
for note in tenor_notes:
    instrument.notes.append(note)

#---------------------
# Save the MIDI file
#---------------------

midi.write("dante_intro.mid")
print("MIDI file 'dante_intro.mid' created.")
