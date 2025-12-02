
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to F minor
key = 'Fm'

# Create instruments for each player
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drumkit')

sax = pretty_midi.Instrument(program=sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

pm.instruments = [drums, piano, bass, sax]

# Define time (in seconds) and note values for 4 bars (160 BPM = 6.0 seconds)
# Bar = 1.5s, beat = 0.375s, eighth note = 0.1875s

#---------------------
# DRUMS - BAR 1
#---------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar is 1.5 seconds, so we'll place notes at 0.1875s intervals
for i in range(8):
    time = i * 0.1875
    if i == 0 or i == 4:   # Kick on 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
    if i == 2 or i == 6:   # Snare on 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1))
    if i % 2 == 0:        # Hihat on every eighth
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1))

#---------------------
# PIANO - BARS 2-4
#---------------------
# Comping on 2 and 4 with 7th chords, unique each measure
# Fm7, Bbm7, Ebm7, Abm7, etc.
# Bar 2: Fm7 (F, Ab, Bb, Db)
# Bar 3: Bbm7 (Bb, D, Eb, F)
# Bar 4: Ebm7 (Eb, Gb, F, Ab)
# Bar 5: Abm7 (Ab, B, Bb, Db)
# Time for each chord: starts on beat 2, duration 1.0s (2 beats)

# Bar 2: Fm7 on beat 2
chord_notes = [pretty_midi.note_number_from_name('F'), pretty_midi.note_number_from_name('A#'),
               pretty_midi.note_number_from_name('Bb'), pretty_midi.note_number_from_name('D#')]
for note in chord_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=1.5, end=2.5))

# Bar 3: Bbm7 on beat 2
chord_notes = [pretty_midi.note_number_from_name('Bb'), pretty_midi.note_number_from_name('D'),
               pretty_midi.note_number_from_name('Eb'), pretty_midi.note_number_from_name('F')]
for note in chord_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=3.0, end=4.0))

# Bar 4: Ebm7 on beat 2
chord_notes = [pretty_midi.note_number_from_name('Eb'), pretty_midi.note_number_from_name('G#'),
               pretty_midi.note_number_from_name('F'), pretty_midi.note_number_from_name('Ab')]
for note in chord_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=4.5, end=5.5))

#---------------------
# BASS - BARS 2-4
#---------------------
# Walking line with chromatic approaches, no repeated notes or intervals
# Bar 2: F, G, Ab, Bb
# Bar 3: Bb, C, Db, Eb
# Bar 4: Eb, F, Gb, Ab

# Bar 2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_number_from_name('F'), start=1.5, end=1.75))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_number_from_name('G'), start=1.75, end=2.0))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_number_from_name('Ab'), start=2.0, end=2.25))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_number_from_name('Bb'), start=2.25, end=2.5))

# Bar 3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_number_from_name('Bb'), start=3.0, end=3.25))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_number_from_name('C'), start=3.25, end=3.5))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_number_from_name('Db'), start=3.5, end=3.75))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_number_from_name('Eb'), start=3.75, end=4.0))

# Bar 4
bass.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_number_from_name('Eb'), start=4.5, end=4.75))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_number_from_name('F'), start=4.75, end=5.0))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_number_from_name('Gb'), start=5.0, end=5.25))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_number_from_name('Ab'), start=5.25, end=5.5))

#---------------------
# SAX - BARS 2-4
#---------------------
# Motif: F, Ab, Bb, rest (whisper)
# Then F, Ab, Bb, Eb (cry)
# Then F, G, Ab, Bb (build)
# Time: start at 1.5s (beat 2 of bar 2)

# First note: F on beat 2
sax.notes.append(pretty_midi.Note(velocity=110, pitch=pretty_midi.note_number_from_name('F'), start=1.5, end=1.75))

# Second note: Ab on beat 3
sax.notes.append(pretty_midi.Note(velocity=110, pitch=pretty_midi.note_number_from_name('Ab'), start=1.75, end=2.0))

# Third note: Bb on beat 4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=pretty_midi.note_number_from_name('Bb'), start=2.0, end=2.25))

# Rest (space)
# No note from 2.25s to 3.0s (half a beat of silence)

# Second phrase: F, Ab, Bb, Eb (build)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=pretty_midi.note_number_from_name('F'), start=3.0, end=3.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=pretty_midi.note_number_from_name('Ab'), start=3.25, end=3.5))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=pretty_midi.note_number_from_name('Bb'), start=3.5, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=pretty_midi.note_number_from_name('Eb'), start=3.75, end=4.0))

# Third phrase: F, G, Ab, Bb (build further)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=pretty_midi.note_number_from_name('F'), start=4.5, end=4.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=pretty_midi.note_number_from_name('G'), start=4.75, end=5.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=pretty_midi.note_number_from_name('Ab'), start=5.0, end=5.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=pretty_midi.note_number_from_name('Bb'), start=5.25, end=5.5))

# Write the MIDI file
pm.write('dante_russo_intro.mid')
