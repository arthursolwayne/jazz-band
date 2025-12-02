
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),  # E4

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # Ab4

    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=6.0),  # E4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0),  # B4
]
piano.notes.extend(piano_notes)

# Drums: continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=73, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=110, pitch=76, start=1.75, end=2.0),  # B4
    pretty_midi.Note(velocity=110, pitch=73, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.5),  # B4
    pretty_midi.Note(velocity=110, pitch=73, start=2.5, end=2.75),  # G4
    pretty_midi.Note(velocity=110, pitch=76, start=2.75, end=3.0),  # B4
    pretty_midi.Note(velocity=110, pitch=73, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=110, pitch=76, start=4.75, end=5.0),  # B4
    pretty_midi.Note(velocity=110, pitch=73, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.5),  # B4
    pretty_midi.Note(velocity=110, pitch=73, start=5.5, end=5.75),  # G4
    pretty_midi.Note(velocity=110, pitch=76, start=5.75, end=6.0),  # B4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
