
import pretty_midi

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.resolution = 480  # Standard resolution

# Set tempo to 160 BPM (60 * 160 / 60 = 160 beats per minute)
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0,螃蟹=0.0)]
pm.tempos = [pretty_midi.TempoChange(tempo=160.0, time=0.0)]

# Define key: F minor (F, Gb, Ab, Bb, B, Db, Eb)
# Root: F (65.41 Hz) => MIDI note 65
key = 'Fm'

# Time in seconds per bar
bar_length = 1.5  # 6 seconds / 4 bars
beat_length = 0.375  # 1.5 / 4

# Create instruments
bass_program = pretty_midi.instrument_name_to_program("Acoustic Bass")
piano_program = pretty_midi.instrument_name_to_program("Acoustic Grand Piano")
drums_program = pretty_midi.instrument_name_to_program("Acoustic Grand Piano")
sax_program = pretty_midi.instrument_name_to_program("Soprano Sax")

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# BAR 1: DRUMS ONLY
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(0, 8):
    if i % 2 == 0:  # Every eighth note
        hihat = pretty_midi.Note(velocity=64, pitch=42, start=i * beat_length, end=(i + 1) * beat_length)
        drums.notes.append(hihat)

# Kick on 1 and 3
kick_times = [0, 2]
for t in kick_times:
    kick = pretty_midi.Note(velocity=100, pitch=36, start=t * beat_length, end=(t + 1) * beat_length)
    drums.notes.append(kick)

# Snare on 2 and 4
snare_times = [1, 3]
for t in snare_times:
    snare = pretty_midi.Note(velocity=100, pitch=38, start=t * beat_length, end=(t + 1) * beat_length)
    drums.notes.append(snare)

# BAR 2: PIANO (Cm7) -> Bbm7 -> Am7b5 -> D7♭9
# Open voicings, resolve on the last chord

# Cm7: C Eb Gb Bb (C:60, Eb:64, Gb:67, Bb:71)
chord1 = [60, 64, 67, 71]
# Bbm7: Bb D F Ab (Bb:71, D:62, F:65, Ab:69)
chord2 = [71, 62, 65, 69]
# Am7b5: A C Eb G (A:69, C:60, Eb:64, G:67)
chord3 = [69, 60, 64, 67]
# D7♭9: D F# Ab C (D:62, F#:67, Ab:69, C:60)
chord4 = [62, 67, 69, 60]

# Comp on 2 and 4
for i, chord in enumerate([chord1, chord2, chord3, chord4]):
    # Only comp on 2 and 4 (beats 2 and 4 of the bar)
    if i % 2 == 1:
        for note in chord:
            piano_note = pretty_midi.Note(velocity=100, pitch=note, start=(i * beat_length) + 0.5, end=(i * beat_length) + 0.75)
            piano.notes.append(piano_note)

# BAR 2: BASS LINE (Fm root, 5th, chromatic approach)
# Fm: F Ab Bb (F:65, Ab:69, Bb:71)
# Walking bass line in Fm: F -> Gb -> Ab -> Bb (MIDI: 65, 67, 69, 71)
bass_notes = [
    65,  # F
    67,  # Gb chromatic approach
    69,  # Ab
    71,  # Bb
]
for i, note in enumerate(bass_notes):
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=i * beat_length, end=(i + 1) * beat_length)
    bass.notes.append(bass_note)

# BAR 3: SAX MELODY (motif - start, leave it hanging, then resolve)
# Fm – melodic motif: F -> Gb -> Ab -> Bb -> F (MIDI: 65, 67, 69, 71, 65)
# Start it and leave it hanging on the 3rd beat (Ab)
motif = [65, 67, 69]  # First 3 notes of the motif
for i, note in enumerate(motif):
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=i * beat_length, end=(i + 1) * beat_length)
    sax.notes.append(sax_note)

# BAR 4: RESOLVE THE MOTIF (Fm, continue bass, piano resolve to D7♭9)
# F -> Gb -> Ab -> Bb -> F (resolve motif)
resolution = [65, 67, 69, 71, 65]
for i, note in enumerate(resolution):
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=i * beat_length, end=(i + 1) * beat_length)
    sax.notes.append(sax_note)

# BAR 4: PIANO (D7♭9)
for note in chord4:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=2 * beat_length + 0.5, end=3 * beat_length + 0.75)
    piano.notes.append(piano_note)

# BAR 4: BASS LINE (resolve to D7♭9)
# D7♭9: D F# Ab C (MIDI: 62, 67, 69, 60)
bass_notes = [
    62,  # D
    67,  # F#
    69,  # Ab
    60,  # C
]
for i, note in enumerate(bass_notes):
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=(2 + i) * beat_length, end=(3 + i) * beat_length)
    bass.notes.append(bass_note)

# Write MIDI to file
pm.write("waynes_intro.mid")
print("MIDI file created: waynes_intro.mid")
