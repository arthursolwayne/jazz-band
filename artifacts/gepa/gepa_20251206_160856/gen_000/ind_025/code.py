
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38), chromatic approach up to G2 (43)
    pretty_midi.Note(velocity=100, pitch=39, start=1.5, end=1.875),  # chromatic approach
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625),  # chromatic approach
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # C#4
]
piano.notes.extend(piano_notes)

# Sax: Motif - short, singable, start it, leave it hanging
# D4 (62), F#4 (67), Bb4 (70), leave it hanging on Bb4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=70, start=2.0, end=2.25),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: walking line (G2-D3, MIDI 43-50)
# Roots and fifths with chromatic approaches
bass_notes = [
    # Bar 3: G2 (43), chromatic approach up to D3 (50)
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # chromatic approach
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75),  # G2
    pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.125),  # chromatic approach
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bm7 (B, D, F#, A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # A4
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation - echo the first motif but with a twist
# Bb4 (70), D4 (62), F#4 (67)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: walking line (D3-G3, MIDI 50-55)
# Roots and fifths with chromatic approaches
bass_notes = [
    # Bar 4: D3 (50), chromatic approach up to G3 (55)
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),  # chromatic approach
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),  # D3
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625),  # chromatic approach
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0),  # G3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: G7 (G, B, D, F#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # F#4
]
piano.notes.extend(piano_notes)

# Sax: Motif finish - return to the original motif and finish it
# D4 (62), F#4 (67), Bb4 (70)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=70, start=5.0, end=5.25),
]
sax.notes.extend(sax_notes)

# Drums: Bar 3-4 (3.0 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
