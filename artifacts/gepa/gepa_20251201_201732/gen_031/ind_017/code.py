
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
# Bass: F2, A2, C3, D3 (walking line)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25), # A2
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625), # C3
    pretty_midi.Note(velocity=100, pitch=80, start=2.625, end=3.0),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875),  # E
]
# Bar 3: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=80, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=82, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # F
])
# Bar 4: C7 (C, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=79, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=84, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=87, start=2.625, end=3.0),  # B
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, G, Ab, Bb (F -> G -> Ab -> Bb) on beats 1, 2, 3, 4 of bar 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=75, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),  # Bb
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
# Bass: F2, A2, C3, D3 (walking line)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125), # C3
    pretty_midi.Note(velocity=100, pitch=80, start=4.125, end=4.5),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (G, B, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=80, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F
]
# Bar 4: C7 (C, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=84, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=87, start=3.375, end=3.75),  # B
])
piano.notes.extend(piano_notes)

# Sax: Motif repeat with variation
# Motif: F, G, Ab, Bb (F -> G -> Ab -> Bb) on beats 1, 2, 3, 4 of bar 4
# With a slight variation to leave it hanging and come back
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=75, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),   # Bb
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

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled
