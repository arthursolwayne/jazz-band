
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),     # hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)    # kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line on D2-G2 (MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)   # G2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0)
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),   # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),     # hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)    # kick on 3
]
drums.notes.extend(drum_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),   # E4
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),   # F4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875),   # F#4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),    # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),    # E4
    pretty_midi.Note(velocity=100, pitch=64, start=2.125, end=2.25),    # F4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.375),    # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.5),     # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.625),     # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.75),     # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=2.875),     # F#4
    pretty_midi.Note(velocity=100, pitch=64, start=2.875, end=3.0)      # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line on D2-G2 (MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # G2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5)   # F2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),   # Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5)
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),     # hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)    # kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line on D2-G2 (MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # D2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # A2
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)   # G2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0)
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),     # hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)    # kick on 3
]
drums.notes.extend(drum_notes)

# Sax: finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),   # E4
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75),   # F4
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=4.875),   # F#4
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0),    # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.125),    # E4
    pretty_midi.Note(velocity=100, pitch=64, start=5.125, end=5.25),    # F4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.375),    # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=5.375, end=5.5),     # G4
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.625),     # A4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.75),     # G4
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=5.875),     # F#4
    pretty_midi.Note(velocity=100, pitch=64, start=5.875, end=6.0)      # F4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
