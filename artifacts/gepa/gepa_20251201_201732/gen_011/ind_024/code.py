
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth
for i in range(0, 4):
    hihat_start = i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: D2 (D2 is MIDI 38), walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.75))  # D2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=39, start=1.75, end=2.0))  # Eb2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=37, start=2.0, end=2.25))  # C2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.5))  # F2

# Piano: Open voicing, D7 (D F# A C#)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0))  # D4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=2.0))  # F#4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0))  # A4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.0))  # C#5

# Sax: Start motif (D4, E4, F#4, D4)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5))

# Bar 3: (3.0 - 4.5s)

# Bass: G2 (G2 is MIDI 43), walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.25))  # G2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=3.25, end=3.5))  # Ab2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.75))  # F2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.0))  # G#2

# Piano: Open voicing, G7 (G B D F)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.5))  # G4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.5))  # B4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.5))  # D5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.5))  # F5

# Sax: Continue motif (G4, A4, B4, G4)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=3.5, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0))

# Bar 4: (4.5 - 6.0s)

# Bass: B2 (B2 is MIDI 46), walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.75))  # B2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=4.75, end=5.0))  # C3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=5.0, end=5.25))  # A2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.5))  # C#3

# Piano: Open voicing, B7 (B D# F# A)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.0))  # B4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=5.0))  # D#5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=5.0))  # F#5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=5.0))  # A5

# Sax: Finish motif (B4, C5, D5, B4)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=5.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=5.0, end=5.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.5))

# Drums: Bar 4 (4.5 - 6.0s)

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125))

# Hihat on every eighth
for i in range(0, 4):
    hihat_start = 4.5 + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('waynes_jam.mid')
