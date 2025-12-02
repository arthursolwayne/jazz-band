
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 2: Full quartet starts
# Bass line (Marcus): Walking line in Fm, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # Fm7 (F)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # Fm7 (Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Fm7 (D)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # Fm7 (G)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # Fm7 (F)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Fm7 (Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Fm7 (D)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Fm7 (G)
]
piano.notes.extend(piano_notes)

# Drums for bar 2
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Sax (Dante): Melody - One short motif, make it sing
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Bar 3: Continue the motif, build tension
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # G
]
sax.notes.extend(sax_notes)

# Bar 4: Resolve the motif, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Drums for bar 3
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=6.0)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Drums for bar 4
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=6.0)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bass line for bar 3
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Bass line for bar 4
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano for bar 3
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # Fm7 (F)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Fm7 (Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Fm7 (D)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Fm7 (G)
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # Fm7 (F)
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # Fm7 (Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # Fm7 (D)
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # Fm7 (G)
]
piano.notes.extend(piano_notes)

# Piano for bar 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # Fm7 (F)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Fm7 (Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Fm7 (D)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # Fm7 (G)
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # Fm7 (F)
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # Fm7 (Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # Fm7 (D)
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # Fm7 (G)
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_intro.mid')
