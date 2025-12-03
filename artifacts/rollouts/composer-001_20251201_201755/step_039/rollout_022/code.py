
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
    # D2 (MIDI 38) on beat 1
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # F#2 (MIDI 41) on beat 2 (chromatic approach to G2)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.125),
    # G2 (MIDI 43) on beat 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5),
    # B2 (MIDI 46) on beat 4 (chromatic approach to C#3)
    pretty_midi.Note(velocity=90, pitch=46, start=2.5, end=2.75),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # C#5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First note: D4 (MIDI 62) on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    # Second note: F#4 (MIDI 67) on beat 2
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.125),
    # Third note: D4 (MIDI 62) on beat 3
    pretty_midi.Note(velocity=110, pitch=62, start=2.125, end=2.5),
    # Fourth note: F#4 (MIDI 67) on beat 4
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.75),
    # Fifth note: A4 (MIDI 71) on beat 4 (end of bar)
    pretty_midi.Note(velocity=110, pitch=71, start=2.75, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # C#3 (MIDI 51) on beat 1 (chromatic approach to D3)
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.375),
    # D3 (MIDI 52) on beat 2
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75),
    # F#3 (MIDI 55) on beat 3
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125),
    # G3 (MIDI 56) on beat 4
    pretty_midi.Note(velocity=90, pitch=56, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 3: G7 (G, B, D, F#)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # F#5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First note: G4 (MIDI 67) on beat 1
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),
    # Second note: B4 (MIDI 71) on beat 2
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.75),
    # Third note: G4 (MIDI 67) on beat 3
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),
    # Fourth note: B4 (MIDI 71) on beat 4
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),
    # Fifth note: D5 (MIDI 74) on beat 4 (end of bar)
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=4.75),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D3 (MIDI 52) on beat 1
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),
    # F#3 (MIDI 55) on beat 2 (chromatic approach to G3)
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.125),
    # G3 (MIDI 56) on beat 3
    pretty_midi.Note(velocity=90, pitch=56, start=5.125, end=5.5),
    # B3 (MIDI 59) on beat 4 (chromatic approach to C#4)
    pretty_midi.Note(velocity=90, pitch=59, start=5.5, end=5.75),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 4: C#7 (C#, E#, G#, B)
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=6.0),  # C#4
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=6.0),  # E#4 (F4)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # G#4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # B4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First note: C#4 (MIDI 63) on beat 1
    pretty_midi.Note(velocity=110, pitch=63, start=4.5, end=4.875),
    # Second note: E#4 (MIDI 68) on beat 2
    pretty_midi.Note(velocity=110, pitch=68, start=4.875, end=5.125),
    # Third note: C#4 (MIDI 63) on beat 3
    pretty_midi.Note(velocity=110, pitch=63, start=5.125, end=5.5),
    # Fourth note: E#4 (MIDI 68) on beat 4
    pretty_midi.Note(velocity=110, pitch=68, start=5.5, end=5.75),
    # Fifth note: G#4 (MIDI 72) on beat 4 (end of bar)
    pretty_midi.Note(velocity=110, pitch=72, start=5.75, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3 (3.0 - 4.5s)
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

# Bar 4 (4.5 - 6.0s)
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
