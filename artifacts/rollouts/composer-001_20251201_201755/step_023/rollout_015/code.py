
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line with chromatic approaches, D2-G2 (MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),  # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # D4 (root)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # F4 (3rd)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=3.0),  # A4 (5th)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # C5 (7th)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - D4 (saxophones often play an octave above bass)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # C5 (resolve)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line with chromatic approaches, D2-G2 (MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),   # Eb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bbm7 (Bb-D-F-Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=4.5),   # Bb4 (root)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=4.5),   # D5 (3rd)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),   # F5 (5th)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),   # Ab5 (7th)
]
piano.notes.extend(piano_notes)

# Sax: Continue motif with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # Ab5 (resolve)
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line with chromatic approaches, D2-G2 (MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=41, start=4.5, end=4.875),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),   # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Gm7 (G-Bb-D-F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),   # G4 (root)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=6.0),   # Bb4 (3rd)
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=6.0),   # D5 (5th)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),   # F5 (7th)
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # F5 (resolve)
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.375),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
