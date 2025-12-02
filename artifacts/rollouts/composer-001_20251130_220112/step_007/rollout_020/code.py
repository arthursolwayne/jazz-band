
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=37, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=36, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=90, pitch=35, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=34, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=90, pitch=33, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=31, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=90, pitch=30, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=90, pitch=29, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875), # Bb
    pretty_midi.Note(velocity=90, pitch=33, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=30, start=1.5, end=1.875), # Ab
    # Bar 3: Bb7
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=2.8125), # Bb
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=2.8125), # D
    pretty_midi.Note(velocity=90, pitch=36, start=2.625, end=2.8125), # F
    pretty_midi.Note(velocity=90, pitch=31, start=2.625, end=2.8125), # Ab
    # Bar 4: Fm7
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=90, pitch=33, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=30, start=3.75, end=4.125), # Ab
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif start
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.6875), # D
    pretty_midi.Note(velocity=110, pitch=50, start=1.6875, end=1.875), # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=53, start=2.625, end=2.8125), # D
    pretty_midi.Note(velocity=110, pitch=50, start=2.8125, end=3.0), # Bb
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=53, start=3.75, end=3.9375), # D
    pretty_midi.Note(velocity=110, pitch=50, start=3.9375, end=4.125), # Bb
    pretty_midi.Note(velocity=110, pitch=46, start=4.125, end=4.3125), # F
    pretty_midi.Note(velocity=110, pitch=43, start=4.3125, end=4.5), # D
    pretty_midi.Note(velocity=110, pitch=40, start=4.5, end=4.6875), # Bb
    pretty_midi.Note(velocity=110, pitch=37, start=4.6875, end=4.875), # F
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.125, end=3.3125),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
