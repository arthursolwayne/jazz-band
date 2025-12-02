
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: Fm7 -> Bb -> Ab -> G
note = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875)  # F
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25)  # Bb
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625)  # Ab
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0)  # G
sax.notes.append(note)

# Bass: Walking line in Fm
note = pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875)  # F
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25)  # G
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625)  # E
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0)  # G
bass.notes.append(note)

# Piano: F7 on beat 2 and 4
note = pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625)  # F
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625)  # C
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625)  # A
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625)  # E
piano.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125)  # F
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125)  # C
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125)  # A
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125)  # E
piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: A -> Bb -> D -> Eb
note = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375)  # A
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75)  # Bb
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125)  # D
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5)  # Eb
sax.notes.append(note)

# Bass: Walking line in Fm
note = pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375)  # Bb
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=58, start=3.375, end=3.75)  # Ab
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125)  # G
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=58, start=4.125, end=4.5)  # Ab
bass.notes.append(note)

# Piano: F7 on beat 2 and 4
note = pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75)  # F
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75)  # C
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75)  # A
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75)  # E
piano.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875)  # F
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875)  # C
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875)  # A
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875)  # E
piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Bb -> F -> F -> F
note = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875)  # Bb
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25)  # F
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625)  # F
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0)  # F
sax.notes.append(note)

# Bass: Walking line in Fm
note = pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875)  # Ab
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25)  # G
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.625)  # Ab
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0)  # G
bass.notes.append(note)

# Piano: F7 on beat 2 and 4
note = pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25)  # F
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25)  # C
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25)  # A
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25)  # E
piano.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0)  # F
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0)  # C
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0)  # A
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0)  # E
piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0)
drums.notes.append(drum_note)

# Bar 3
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5)
drums.notes.append(drum_note)

# Bar 4
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0)
drums.notes.append(drum_note)

# Add hihat on every eighth
for i in range(0, 6, 0.375):
    if i >= 1.5 and i < 6.0:
        note = pretty_midi.Note(velocity=100, pitch=42, start=i, end=i + 0.375)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
