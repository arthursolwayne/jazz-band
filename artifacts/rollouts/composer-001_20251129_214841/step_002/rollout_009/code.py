
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    # Hi-hat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # E5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # B4
]
sax.notes.extend(sax_notes)

# Bass line (walking line with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # C3
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # C#3
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),  # D3
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.5),  # D#3
    pretty_midi.Note(velocity=80, pitch=52, start=2.5, end=2.75),  # E3
    pretty_midi.Note(velocity=80, pitch=51, start=2.75, end=3.0),  # D#3
]
bass.notes.extend(bass_notes)

# Piano comping (7th chords on 2 and 4)
piano_notes = [
    # Bar 2, beat 2 (C7)
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=2.0),  # C4
    pretty_midi.Note(velocity=90, pitch=74, start=1.75, end=2.0),  # E4
    pretty_midi.Note(velocity=90, pitch=76, start=1.75, end=2.0),  # G4
    pretty_midi.Note(velocity=90, pitch=79, start=1.75, end=2.0),  # B4
    # Bar 2, beat 4 (C7)
    pretty_midi.Note(velocity=90, pitch=72, start=2.75, end=3.0),  # C4
    pretty_midi.Note(velocity=90, pitch=74, start=2.75, end=3.0),  # E4
    pretty_midi.Note(velocity=90, pitch=76, start=2.75, end=3.0),  # G4
    pretty_midi.Note(velocity=90, pitch=79, start=2.75, end=3.0),  # B4
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone continues motif, shifted up
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=100, pitch=70, start=3.25, end=3.5),  # E5
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75),  # F5
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.0),  # E5
    pretty_midi.Note(velocity=100, pitch=68, start=4.0, end=4.25),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # D5
]
sax.notes.extend(sax_notes)

# Bass line (walking line with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25),  # F3
    pretty_midi.Note(velocity=80, pitch=54, start=3.25, end=3.5),  # F#3
    pretty_midi.Note(velocity=80, pitch=55, start=3.5, end=3.75),  # G3
    pretty_midi.Note(velocity=80, pitch=56, start=3.75, end=4.0),  # G#3
    pretty_midi.Note(velocity=80, pitch=57, start=4.0, end=4.25),  # A3
    pretty_midi.Note(velocity=80, pitch=56, start=4.25, end=4.5),  # G#3
]
bass.notes.extend(bass_notes)

# Piano comping (7th chords on 2 and 4)
piano_notes = [
    # Bar 3, beat 2 (D7)
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),  # D4
    pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.5),  # F4
    pretty_midi.Note(velocity=90, pitch=78, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=90, pitch=81, start=3.25, end=3.5),  # C5
    # Bar 3, beat 4 (D7)
    pretty_midi.Note(velocity=90, pitch=74, start=4.25, end=4.5),  # D4
    pretty_midi.Note(velocity=90, pitch=76, start=4.25, end=4.5),  # F4
    pretty_midi.Note(velocity=90, pitch=78, start=4.25, end=4.5),  # A4
    pretty_midi.Note(velocity=90, pitch=81, start=4.25, end=4.5),  # C5
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone resolves motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # E5
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),  # F#5
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25),  # G5
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # F#5
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # E5
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # D5
]
sax.notes.extend(sax_notes)

# Bass line (walking line with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=58, start=4.5, end=4.75),  # B3
    pretty_midi.Note(velocity=80, pitch=59, start=4.75, end=5.0),  # C4
    pretty_midi.Note(velocity=80, pitch=60, start=5.0, end=5.25),  # C#4
    pretty_midi.Note(velocity=80, pitch=61, start=5.25, end=5.5),  # D4
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.75),  # D#4
    pretty_midi.Note(velocity=80, pitch=61, start=5.75, end=6.0),  # D4
]
bass.notes.extend(bass_notes)

# Piano comping (7th chords on 2 and 4)
piano_notes = [
    # Bar 4, beat 2 (E7)
    pretty_midi.Note(velocity=90, pitch=76, start=4.75, end=5.0),  # G4
    pretty_midi.Note(velocity=90, pitch=78, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=90, pitch=80, start=4.75, end=5.0),  # B4
    pretty_midi.Note(velocity=90, pitch=83, start=4.75, end=5.0),  # D5
    # Bar 4, beat 4 (E7)
    pretty_midi.Note(velocity=90, pitch=76, start=5.75, end=6.0),  # G4
    pretty_midi.Note(velocity=90, pitch=78, start=5.75, end=6.0),  # A4
    pretty_midi.Note(velocity=90, pitch=80, start=5.75, end=6.0),  # B4
    pretty_midi.Note(velocity=90, pitch=83, start=5.75, end=6.0),  # D5
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),
    drums.notes.extend([
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
        pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),
    ])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
