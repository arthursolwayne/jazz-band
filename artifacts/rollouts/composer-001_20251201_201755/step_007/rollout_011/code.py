
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F minor
bass_notes = [
    # F2 (root) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.125),
    # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=73, start=2.125, end=2.5),
    # F2 (root)
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.875)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.5),
    pretty_midi.Note(velocity=100, pitch=72, start=2.125, end=2.5),
    pretty_midi.Note(velocity=100, pitch=76, start=2.125, end=2.5),
    pretty_midi.Note(velocity=100, pitch=79, start=2.125, end=2.5),
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=80, start=2.625, end=3.0)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, leave it hanging
# F (71), A (76), G (75), F (71)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=76, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=75, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5)
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Same pattern as Bar 1
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
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in F minor
bass_notes = [
    # F2 (root) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.125),
    # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=73, start=5.125, end=5.5),
    # F2 (root)
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.875)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on last bar
# Bar 4: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.875)
]
piano.notes.extend(piano_notes)

# Sax: Return to finish motif
# F (71), A (76), G (75), F (71)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=76, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=75, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.5)
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
