
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Eb2 on 2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2 on 3
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),  # F2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: Dmaj7 (D, F#, A, C#)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),

    # Bar 3: Em7 (E, G, B, D)
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=3.0),

    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (D4), E (E4), F# (F#4), D (D4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (3.0 - 6.0s)

# Bass: Walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2 on 1
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # Eb2 on 2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125), # G2 on 3
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5),  # F2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif (finish it in bar 4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),
]
sax.notes.extend(sax_notes)

# Bar 4: Drums (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
