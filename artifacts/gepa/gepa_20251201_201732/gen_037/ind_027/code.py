
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1 (0.0 - 1.5s): Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = i * 0.375
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.125, end=time + 0.25)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(note)

# Bar 2 (1.5 - 3.0s): Full quartet. Sax takes the melody
# Sax: F5 (77) -> G5 (78) -> A5 (79) -> G5 (78), then rest
note = pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=78, start=1.75, end=2.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=79, start=2.0, end=2.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=78, start=2.25, end=2.5)
sax.notes.append(note)

# Bass (Bar 2): Walking line (F2 -> G2 -> A2 -> G2)
note = pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=44, start=1.75, end=2.0)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=45, start=2.0, end=2.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.5)
bass.notes.append(note)

# Piano (Bar 2): Open voicing F7 (F-A-C-E)
note = pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.75)
piano.notes.append(note)

# Bar 3 (3.0 - 4.5s): Sax continues with variation
note = pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=78, start=3.25, end=3.5)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=79, start=3.5, end=3.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=78, start=3.75, end=4.0)
sax.notes.append(note)

# Bass (Bar 3): Walking line (F2 -> G2 -> A2 -> G2)
note = pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=44, start=3.25, end=3.5)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=45, start=3.5, end=3.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.0)
bass.notes.append(note)

# Piano (Bar 3): Open voicing Bm7 (B-D-F#-A)
note = pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=86, start=3.0, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=89, start=3.0, end=3.25)
piano.notes.append(note)

# Bar 4 (4.5 - 6.0s): Sax returns to original motif
note = pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=78, start=4.75, end=5.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=79, start=5.0, end=5.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=78, start=5.25, end=5.5)
sax.notes.append(note)

# Bass (Bar 4): Walking line (F2 -> G2 -> A2 -> G2)
note = pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=44, start=4.75, end=5.0)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=45, start=5.0, end=5.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.5)
bass.notes.append(note)

# Piano (Bar 4): Open voicing F7 (F-A-C-E)
note = pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.75)
piano.notes.append(note)

# Drums continue in Bar 2-4:
for i in range(4, 8):
    time = (i - 4) * 0.375 + 1.5
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.125, end=time + 0.25)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(note)

for i in range(4, 8):
    time = (i - 4) * 0.375 + 3.0
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.125, end=time + 0.25)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(note)

for i in range(4, 8):
    time = (i - 4) * 0.375 + 4.5
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.125, end=time + 0.25)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
