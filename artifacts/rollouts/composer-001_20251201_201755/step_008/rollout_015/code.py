
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

# Drums - Bar 1
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 1, 2, 3]:
    note = pretty_midi.Note(velocity=100, pitch=42, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drums.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75)
drums.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)
drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass - Bar 2 (F root, chromatic approach to G)
note = pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875)  # F (D2)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25)  # F#
note = pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625)  # G
note = pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0)  # F
bass.notes.append(note)
bass.notes.append(note)
bass.notes.append(note)
bass.notes.append(note)

# Piano - Bar 2 (Fmaj7)
note = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0)  # F (C4)
note = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0)  # A (E4)
note = pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0)  # C (G4)
note = pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0)  # E (B4)
piano.notes.append(note)
piano.notes.append(note)
piano.notes.append(note)
piano.notes.append(note)

# Sax - Bar 2 (Motif: F - G - C - B)
note = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875)  # F
note = pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25)  # G
note = pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625)  # C
note = pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0)  # B
sax.notes.append(note)
sax.notes.append(note)
sax.notes.append(note)
sax.notes.append(note)

# Drums - Bar 2
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 1, 2, 3]:
    note = pretty_midi.Note(velocity=100, pitch=42, start=(beat + 4) * 0.375, end=(beat + 5) * 0.375)
    drums.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drums.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drums.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.999)
drums.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375)
drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass - Bar 3 (A root, chromatic approach to B)
note = pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.375)  # A
note = pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75)  # A#
note = pretty_midi.Note(velocity=100, pitch=75, start=3.75, end=4.125)  # B
note = pretty_midi.Note(velocity=100, pitch=73, start=4.125, end=4.5)  # A
bass.notes.append(note)
bass.notes.append(note)
bass.notes.append(note)
bass.notes.append(note)

# Piano - Bar 3 (Amaj7)
note = pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=4.5)  # A
note = pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5)  # C
note = pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5)  # E
note = pretty_midi.Note(velocity=100, pitch=80, start=3.0, end=4.5)  # G
piano.notes.append(note)
piano.notes.append(note)
piano.notes.append(note)
piano.notes.append(note)

# Sax - Bar 3 (Motif: A - B - E - D)
note = pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375)  # A
note = pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75)  # B
note = pretty_midi.Note(velocity=100, pitch=75, start=3.75, end=4.125)  # E
note = pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5)  # D
sax.notes.append(note)
sax.notes.append(note)
sax.notes.append(note)
sax.notes.append(note)

# Drums - Bar 3
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 1, 2, 3]:
    note = pretty_midi.Note(velocity=100, pitch=42, start=(beat + 8) * 0.375, end=(beat + 9) * 0.375)
    drums.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drums.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
drums.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.499)
drums.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875)
drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass - Bar 4 (F root, chromatic approach to G)
note = pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875)  # F
note = pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25)  # F#
note = pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625)  # G
note = pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0)  # F
bass.notes.append(note)
bass.notes.append(note)
bass.notes.append(note)
bass.notes.append(note)

# Piano - Bar 4 (Fmaj7)
note = pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0)  # F
note = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0)  # A
note = pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0)  # C
note = pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0)  # E
piano.notes.append(note)
piano.notes.append(note)
piano.notes.append(note)
piano.notes.append(note)

# Sax - Bar 4 (Motif: F - G - C - B, return to start)
note = pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875)  # F
note = pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25)  # G
note = pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625)  # C
note = pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0)  # B
sax.notes.append(note)
sax.notes.append(note)
sax.notes.append(note)
sax.notes.append(note)

# Drums - Bar 4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 1, 2, 3]:
    note = pretty_midi.Note(velocity=100, pitch=42, start=(beat + 12) * 0.375, end=(beat + 13) * 0.375)
    drums.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drums.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
drums.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.999)
drums.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375)
drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
