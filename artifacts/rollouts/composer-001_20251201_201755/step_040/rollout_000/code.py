
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
    # D2 (MIDI 38) on 1
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # Eb2 (MIDI 39) approach to G2 (MIDI 43) on 2
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.0),
    # G2 (MIDI 43) on 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),
    # Ab2 (MIDI 44) approach to C2 (MIDI 40) on 4
    pretty_midi.Note(velocity=90, pitch=44, start=2.375, end=2.625),
    # C2 (MIDI 40) on 4
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # Eb5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First note: F4 (MIDI 65) on 1
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),
    # Second note: Ab4 (MIDI 69) on 2
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.125),
    # Third note: C5 (MIDI 72) on 3
    pretty_midi.Note(velocity=110, pitch=72, start=2.125, end=2.5),
    # Fourth note: Eb5 (MIDI 76) on 4
    pretty_midi.Note(velocity=110, pitch=76, start=2.5, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # C2 (MIDI 40) on 1
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),
    # Db2 (MIDI 41) approach to Eb2 (MIDI 43) on 2
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.625),
    # Eb2 (MIDI 43) on 3
    pretty_midi.Note(velocity=90, pitch=43, start=3.625, end=4.0),
    # F2 (MIDI 45) approach to G2 (MIDI 43) on 4
    pretty_midi.Note(velocity=90, pitch=45, start=4.0, end=4.25),
    # G2 (MIDI 43) on 4
    pretty_midi.Note(velocity=90, pitch=43, start=4.25, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # F5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # Ab5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First note: Bb4 (MIDI 62) on 1
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),
    # Second note: D5 (MIDI 67) on 2
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),
    # Third note: F5 (MIDI 71) on 3
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.125),
    # Fourth note: Ab5 (MIDI 76) on 4
    pretty_midi.Note(velocity=110, pitch=76, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # G2 (MIDI 43) on 1
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),
    # Ab2 (MIDI 44) approach to Bb2 (MIDI 46) on 2
    pretty_midi.Note(velocity=90, pitch=44, start=4.875, end=5.125),
    # Bb2 (MIDI 46) on 3
    pretty_midi.Note(velocity=90, pitch=46, start=5.125, end=5.5),
    # B2 (MIDI 47) approach to C2 (MIDI 40) on 4
    pretty_midi.Note(velocity=90, pitch=47, start=5.5, end=5.75),
    # C2 (MIDI 40) on 4
    pretty_midi.Note(velocity=90, pitch=40, start=5.75, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Eb7 (Eb, G, Bb, Db)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=6.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # Bb5
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # Db5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First note: Eb4 (MIDI 61) on 1
    pretty_midi.Note(velocity=110, pitch=61, start=4.5, end=4.875),
    # Second note: G5 (MIDI 67) on 2
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),
    # Third note: Bb5 (MIDI 71) on 3
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625),
    # Fourth note: Db5 (MIDI 69) on 4
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
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
