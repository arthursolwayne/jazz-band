
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25), # C#
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=4.875, end=5.25), # C#
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # F# on 2
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # F# on 2
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # F# on 2
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # E
]
piano.notes.extend(piano_notes)

# Drums: full bar
for bar_start in [1.5, 3.0, 4.5]:
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75),  # Hihat on 2
        pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125),  # Snare on 3
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),  # Hihat on 4
    ]
    drums.notes.extend(drum_notes)

# Saxophone - Dante: motif in D (D, F#, B, E), short phrase, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),   # E
]
sax.notes.extend(sax_notes)

# Repeat the motif later with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.125, end=3.25),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5),   # E
]
sax.notes.extend(sax_notes)

# Final resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0),   # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
