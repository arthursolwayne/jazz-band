
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
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: Fm (F, Ab, D)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.125),  # Ab2
    pretty_midi.Note(velocity=100, pitch=43, start=2.125, end=2.5),  # D2
    pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=2.875),  # C#2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # D5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.125),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=2.125, end=2.5),  # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.625),  # D2
    pretty_midi.Note(velocity=100, pitch=38, start=3.625, end=4.0),  # F2
    pretty_midi.Note(velocity=100, pitch=40, start=4.0, end=4.375),  # Ab2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=56, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),  # Ab4
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),  # F4
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # F4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.125),  # G2
    pretty_midi.Note(velocity=100, pitch=40, start=5.125, end=5.5),  # Bb2
    pretty_midi.Note(velocity=100, pitch=43, start=5.5, end=5.875),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=54, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=54, start=4.5, end=4.875),  # D4
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),  # A4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
