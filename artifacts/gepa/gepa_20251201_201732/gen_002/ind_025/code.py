
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625), # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),  # F2 (chromatic approach)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # A2 (root)
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.125), # D3 (fifth)
    pretty_midi.Note(velocity=90, pitch=46, start=4.125, end=4.5),  # C3 (chromatic approach)
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625), # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0),  # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E♭)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # E♭4

    # Bar 3: B♭7 (B♭ D F A♭)
    pretty_midi.Note(velocity=100, pitch=61, start=2.0, end=2.5),  # B♭4
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.5),  # A♭4

    # Bar 4: E7 (E G# B D)
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0),  # E4
    pretty_midi.Note(velocity=100, pitch=68, start=2.5, end=3.0),  # G#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # D4
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25)
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.875, end=start + 2.25)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.25, end=start + 2.625)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.625, end=start + 3.0)

drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4 - A♭4 - B♭4 - C5 (1.5 - 2.25s), then hold on C5 until 3.0s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # A♭4
    pretty_midi.Note(velocity=110, pitch=68, start=2.25, end=2.625),  # B♭4
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=3.0),   # C5
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=4.0),     # C5 (hold)
    pretty_midi.Note(velocity=110, pitch=69, start=4.0, end=4.5),     # B4
    pretty_midi.Note(velocity=110, pitch=68, start=4.5, end=5.0),     # B♭4
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.5),     # A♭4
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=6.0),     # F4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
