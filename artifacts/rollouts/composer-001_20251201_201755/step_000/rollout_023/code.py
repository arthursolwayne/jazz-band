
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Roots and fifths with chromatic approaches
# F7 (F, C, Bb, E)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25),  # C3
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # Bb3
    pretty_midi.Note(velocity=90, pitch=79, start=2.625, end=3.0),   # E3
    pretty_midi.Note(velocity=90, pitch=75, start=3.0, end=3.375),   # Bb3 (chromatic)
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),  # C3
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=4.125),  # D3
    pretty_midi.Note(velocity=90, pitch=79, start=4.125, end=4.5),   # E3
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=4.875),   # D3
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # C3
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),  # Bb3
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),   # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    # Bar 2: F7
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),  # E5
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),   # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=3.0),   # D5
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),   # F5
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),   # Ab5
    # Bar 4: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),   # E4
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.75),   # G#4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.75),   # B4
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.75),   # D5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65) - Bb (69) - F (65) - Bb (69), then rest
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25),  # Bb4
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),   # Bb4
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),   # F4
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),  # Bb4
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),   # Bb4
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
