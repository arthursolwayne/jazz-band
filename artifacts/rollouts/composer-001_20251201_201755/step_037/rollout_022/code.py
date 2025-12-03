
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
    # Fm root (D2, MIDI 38) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=37, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Bb (Fm 3rd, G2, MIDI 43)
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=100, pitch=44, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=100, pitch=43, start=2.375, end=2.5),
    # D (Fm 5th, F#2, MIDI 41)
    pretty_midi.Note(velocity=100, pitch=41, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=100, pitch=40, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=100, pitch=41, start=2.875, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, D, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0),  # F (MIDI 53)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.0),  # Ab (MIDI 50)
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.0),  # D (MIDI 57)
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=2.0),  # Eb (MIDI 51)
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=58, start=2.0, end=2.5),  # Bb (MIDI 58)
    pretty_midi.Note(velocity=100, pitch=57, start=2.0, end=2.5),  # D (MIDI 57)
    pretty_midi.Note(velocity=100, pitch=53, start=2.0, end=2.5),  # F (MIDI 53)
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.5),  # Ab (MIDI 50)
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0),  # C (MIDI 60)
    pretty_midi.Note(velocity=100, pitch=51, start=2.5, end=3.0),  # Eb (MIDI 51)
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),  # G (MIDI 62)
    pretty_midi.Note(velocity=100, pitch=58, start=2.5, end=3.0),  # Bb (MIDI 58)
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Ab, D, Eb (MIDI 53, 50, 57, 51)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=50, start=1.875, end=2.125),  # Ab
    pretty_midi.Note(velocity=110, pitch=57, start=2.125, end=2.5),  # D
    pretty_midi.Note(velocity=110, pitch=51, start=2.5, end=2.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=53, start=2.75, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Kick on 1 and 3
drum_notes = [
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

# Bar 4: Drums (4.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
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

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Fm root (D2, MIDI 38) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=37, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    # Bb (Fm 3rd, G2, MIDI 43)
    pretty_midi.Note(velocity=100, pitch=43, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=100, pitch=44, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=100, pitch=43, start=3.875, end=4.0),
    # D (Fm 5th, F#2, MIDI 41)
    pretty_midi.Note(velocity=100, pitch=41, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=100, pitch=40, start=4.1875, end=4.375),
    pretty_midi.Note(velocity=100, pitch=41, start=4.375, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.5),  # Bb (MIDI 58)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.5),  # D (MIDI 57)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.5),  # F (MIDI 53)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.5),  # Ab (MIDI 50)
]
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=4.0),  # C (MIDI 60)
    pretty_midi.Note(velocity=100, pitch=51, start=3.5, end=4.0),  # Eb (MIDI 51)
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=4.0),  # G (MIDI 62)
    pretty_midi.Note(velocity=100, pitch=58, start=3.5, end=4.0),  # Bb (MIDI 58)
])
# Bar 4: Resolving chord (Fm7)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=53, start=4.0, end=4.5),  # F (MIDI 53)
    pretty_midi.Note(velocity=100, pitch=50, start=4.0, end=4.5),  # Ab (MIDI 50)
    pretty_midi.Note(velocity=100, pitch=57, start=4.0, end=4.5),  # D (MIDI 57)
    pretty_midi.Note(velocity=100, pitch=51, start=4.0, end=4.5),  # Eb (MIDI 51)
])
piano.notes.extend(piano_notes)

# Bar 4: Sax (4.5 - 6.0s)
# Repeat the motif and end on F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=50, start=4.875, end=5.125),  # Ab
    pretty_midi.Note(velocity=110, pitch=57, start=5.125, end=5.5),  # D
    pretty_midi.Note(velocity=110, pitch=51, start=5.5, end=5.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=53, start=5.75, end=6.0),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
