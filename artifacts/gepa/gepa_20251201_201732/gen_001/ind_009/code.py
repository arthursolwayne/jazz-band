
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = i * 0.375
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.25)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.625)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line (F2, G2, Ab2, A2, Bb2, B2, C3, Db3, etc.)
bass_notes = [72, 73, 74, 76, 77, 78, 79, 81]
for i, pitch in enumerate(bass_notes):
    time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
note = pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.5 + 0.375)
piano.notes.append(note)

# Bar 3: G7 (G, B, D, F)
note = pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.25 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=2.25 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=84, start=2.25, end=2.25 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.25 + 0.375)
piano.notes.append(note)

# Bar 4: Cm7 (C, Eb, G, Bb)
note = pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.0 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.0 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.0 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.0 + 0.375)
piano.notes.append(note)

# Dante: Tenor sax - one short motif, make it sing
# Start on F, then move to Ab, then back to F (F - Ab - F) in bar 2
note = pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.5 + 0.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=1.625, end=1.625 + 0.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=1.75 + 0.125)
sax.notes.append(note)

# Bar 3: Add a rest, leave it hanging
# Bar 4: Return to F, then resolve to Ab and back to F (F - Ab - F)
note = pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.0 + 0.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=3.125, end=3.125 + 0.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.25 + 0.125)
sax.notes.append(note)

# Drums for bars 2-4
for i in range(6):
    time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.25)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.625)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
