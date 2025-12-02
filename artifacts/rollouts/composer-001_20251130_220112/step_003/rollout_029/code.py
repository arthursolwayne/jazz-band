
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Start of the melody (1.5 - 3.0s)
# Sax: F (F4), Bb (Bb4), Eb (Eb4), Ab (Ab4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # Eb4
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # Ab4
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=1.5, end=1.75),  # F3
    pretty_midi.Note(velocity=80, pitch=48, start=1.75, end=2.0),  # G3
    pretty_midi.Note(velocity=80, pitch=45, start=2.0, end=2.25),  # E3
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.5),  # D3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (1.75 - 2.0)
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # Bb4
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # C5 (7th)
    # Bar 2, beat 4 (2.25 - 2.5)
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),  # Ab3
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # Bb3
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # C4
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # D4 (7th)
]
piano.notes.extend(piano_notes)

# Bar 3: Continue the melody (3.0 - 4.5s)
# Sax: F (F4), Bb (Bb4), Eb (Eb4), Ab (Ab4) again but with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # Ab4
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.25),  # F3
    pretty_midi.Note(velocity=80, pitch=48, start=3.25, end=3.5),  # G3
    pretty_midi.Note(velocity=80, pitch=45, start=3.5, end=3.75),  # E3
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.0),  # D3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2 (3.25 - 3.5)
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),  # C5 (7th)
    # Bar 3, beat 4 (3.75 - 4.0)
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),  # Ab3
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # Bb3
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # C4
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # D4 (7th)
]
piano.notes.extend(piano_notes)

# Bar 4: End of the melody (4.5 - 6.0s)
# Sax: F (F4), Bb (Bb4), Eb (Eb4), Ab (Ab4) with a descending run
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # Eb4
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # Ab4
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.75),  # F3
    pretty_midi.Note(velocity=80, pitch=48, start=4.75, end=5.0),  # G3
    pretty_midi.Note(velocity=80, pitch=45, start=5.0, end=5.25),  # E3
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.5),  # D3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2 (4.75 - 5.0)
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # Bb4
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),  # C5 (7th)
    # Bar 4, beat 4 (5.25 - 5.5)
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),  # Ab3
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # Bb3
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),  # C4
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # D4 (7th)
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4, continue the pattern
for bar in range(2, 5):
    start_time = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.0, end=start_time + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * 0.1875, end=start_time + (i + 1) * 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
