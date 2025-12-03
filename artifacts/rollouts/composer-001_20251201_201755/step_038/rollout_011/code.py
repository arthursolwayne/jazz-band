
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
    # F#2 (MIDI 41) chromatic approach to G2 (MIDI 43)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.0),
    # G2 (MIDI 43) on beat 2
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),
    # Bb2 (MIDI 42) chromatic approach to C#2 (MIDI 40)
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5),
    # C#2 (MIDI 40) on beat 3
    pretty_midi.Note(velocity=90, pitch=40, start=2.5, end=2.875),
    # D2 (MIDI 38) chromatic approach to Eb2 (MIDI 39)
    pretty_midi.Note(velocity=90, pitch=38, start=2.875, end=3.0),
    # Eb2 (MIDI 39) on beat 4
    pretty_midi.Note(velocity=90, pitch=39, start=3.0, end=3.375),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C#4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First motif: D4 (62) on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    # F#4 (67) on beat 2
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.375),
    # D4 (62) on beat 3
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.875),
    # Bb4 (70) on beat 4 (resolve)
    pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.375),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # G2 (MIDI 43) on beat 1
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    # Bb2 (MIDI 42) chromatic approach to C#2 (MIDI 40)
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5),
    # C#2 (MIDI 40) on beat 2
    pretty_midi.Note(velocity=90, pitch=40, start=3.5, end=3.875),
    # D2 (MIDI 38) chromatic approach to Eb2 (MIDI 39)
    pretty_midi.Note(velocity=90, pitch=38, start=3.875, end=4.0),
    # Eb2 (MIDI 39) on beat 3
    pretty_midi.Note(velocity=90, pitch=39, start=4.0, end=4.375),
    # F#2 (MIDI 41) chromatic approach to G2 (MIDI 43)
    pretty_midi.Note(velocity=90, pitch=41, start=4.375, end=4.5),
    # G2 (MIDI 43) on beat 4
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bm7 (B, D, F#, A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # A4
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, leave it hanging
sax_notes = [
    # Bb4 (70) on beat 1
    pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.375),
    # D5 (62) on beat 2
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.875),
    # F#4 (67) on beat 3
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.375),
    # Bb4 (70) on beat 4 (resolve)
    pretty_midi.Note(velocity=110, pitch=70, start=4.5, end=4.875),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # G2 (MIDI 43) on beat 1
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),
    # Bb2 (MIDI 42) chromatic approach to C#2 (MIDI 40)
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0),
    # C#2 (MIDI 40) on beat 2
    pretty_midi.Note(velocity=90, pitch=40, start=5.0, end=5.375),
    # D2 (MIDI 38) chromatic approach to Eb2 (MIDI 39)
    pretty_midi.Note(velocity=90, pitch=38, start=5.375, end=5.5),
    # Eb2 (MIDI 39) on beat 3
    pretty_midi.Note(velocity=90, pitch=39, start=5.5, end=5.875),
    # F#2 (MIDI 41) chromatic approach to G2 (MIDI 43)
    pretty_midi.Note(velocity=90, pitch=41, start=5.875, end=6.0),
    # G2 (MIDI 43) on beat 4
    pretty_midi.Note(velocity=90, pitch=43, start=6.0, end=6.375),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: G7 (G, B, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # F4
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    # G4 (67) on beat 1
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),
    # Bb4 (70) on beat 2
    pretty_midi.Note(velocity=110, pitch=70, start=5.0, end=5.375),
    # D5 (62) on beat 3
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.875),
    # F#4 (67) on beat 4 (resolve)
    pretty_midi.Note(velocity=110, pitch=67, start=6.0, end=6.375),
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125),
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

# Write the MIDI file
# midi.write disabled
