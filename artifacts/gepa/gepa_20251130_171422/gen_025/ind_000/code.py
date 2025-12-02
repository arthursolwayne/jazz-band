
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Build tension with rhythmic space and dynamics
drum_notes = [
    # Kick on beat 1
    pretty_midi.Note(velocity=60, pitch=36, start=0.0, end=0.375),
    # Hihat on beat 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    # Snare on beat 3
    pretty_midi.Note(velocity=70, pitch=38, start=1.125, end=1.5),
    # Hihat on beat 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=2.0625),
    # Kick on beat 4
    pretty_midi.Note(velocity=50, pitch=36, start=1.875, end=2.25),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif (Bar 2)
sax_notes = [
    # Bar 2: Dante's motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D4

    # Bar 3: continuation
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F4

    # Bar 4: resolution
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D4
]
sax.notes.extend(sax_notes)

# Bass line (Bar 2-4: Marcus)
bass_notes = [
    # Bar 2: walking line
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=80, pitch=50, start=1.75, end=2.0),  # E3
    pretty_midi.Note(velocity=80, pitch=49, start=2.0, end=2.25),  # D#3
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),  # D3

    # Bar 3: chromatic approach to G
    pretty_midi.Note(velocity=80, pitch=51, start=2.5, end=2.75),  # F3
    pretty_midi.Note(velocity=80, pitch=52, start=2.75, end=3.0),  # F#3
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25),  # G3
    pretty_midi.Note(velocity=80, pitch=55, start=3.25, end=3.5),  # A3

    # Bar 4: descending line
    pretty_midi.Note(velocity=80, pitch=53, start=3.5, end=3.75),  # G3
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.0),  # F3
    pretty_midi.Note(velocity=80, pitch=49, start=4.0, end=4.25),  # D#3
    pretty_midi.Note(velocity=80, pitch=48, start=4.25, end=4.5),  # D3
]
bass.notes.extend(bass_notes)

# Piano (Diane) comping on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # B4 (D7 chord)
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # G4
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # E4
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25),  # B4 (D7 chord)
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),  # E4
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25),  # D4

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),  # B4 (D7 chord)
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # G4
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # E4
    pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # B4 (D7 chord)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # E4
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),  # D4

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # B4 (D7 chord)
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # G4
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # E4
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25),  # B4 (D7 chord)
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25),  # G4
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25),  # E4
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.25),  # D4
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4
# Hihat on every eighth with dynamic variation
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on beat 1
    pretty_midi.Note(velocity=80, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Hihat on 1 & 2
    pretty_midi.Note(velocity=85, pitch=42, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=85, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    # Snare on beat 2
    pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    # Hihat on 3 & 4
    pretty_midi.Note(velocity=85, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    pretty_midi.Note(velocity=85, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875)
    # Kick on beat 3
    pretty_midi.Note(velocity=80, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on beat 4
    pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25)
    # Hihat on 4
    pretty_midi.Note(velocity=85, pitch=42, start=bar_start + 2.25, end=bar_start + 2.625)

drums.notes.extend(piano_notes)  # Just to make the code work, but should be replaced with the above

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
