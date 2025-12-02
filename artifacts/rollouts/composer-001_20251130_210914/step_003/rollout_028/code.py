
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.6875, end=1.875), # Gb
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.0625), # E
    pretty_midi.Note(velocity=100, pitch=42, start=2.0625, end=2.25), # D
    pretty_midi.Note(velocity=100, pitch=44, start=2.25, end=2.4375), # F
    pretty_midi.Note(velocity=100, pitch=46, start=2.4375, end=2.625), # Ab
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=2.8125), # Gb
    pretty_midi.Note(velocity=100, pitch=44, start=2.8125, end=3.0), # F

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.1875), # F
    pretty_midi.Note(velocity=100, pitch=45, start=3.1875, end=3.375), # Gb
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.5625), # E
    pretty_midi.Note(velocity=100, pitch=42, start=3.5625, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=3.9375), # F
    pretty_midi.Note(velocity=100, pitch=46, start=3.9375, end=4.125), # Ab
    pretty_midi.Note(velocity=100, pitch=45, start=4.125, end=4.3125), # Gb
    pretty_midi.Note(velocity=100, pitch=44, start=4.3125, end=4.5), # F

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.6875), # F
    pretty_midi.Note(velocity=100, pitch=45, start=4.6875, end=4.875), # Gb
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.0625), # E
    pretty_midi.Note(velocity=100, pitch=42, start=5.0625, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=44, start=5.25, end=5.4375), # F
    pretty_midi.Note(velocity=100, pitch=46, start=5.4375, end=5.625), # Ab
    pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=5.8125), # Gb
    pretty_midi.Note(velocity=100, pitch=44, start=5.8125, end=6.0), # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=100, pitch=46, start=1.5, end=1.6875), # Ab
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.6875), # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.6875), # Db

    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.4375), # F
    pretty_midi.Note(velocity=100, pitch=46, start=2.25, end=2.4375), # Ab
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.4375), # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.4375), # Db

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875), # F
    pretty_midi.Note(velocity=100, pitch=46, start=3.0, end=3.1875), # Ab
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.1875), # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.1875), # Db

    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375), # F
    pretty_midi.Note(velocity=100, pitch=46, start=3.75, end=3.9375), # Ab
    pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=3.9375), # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=3.9375), # Db

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875), # F
    pretty_midi.Note(velocity=100, pitch=46, start=4.5, end=4.6875), # Ab
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.6875), # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.6875), # Db

    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375), # F
    pretty_midi.Note(velocity=100, pitch=46, start=5.25, end=5.4375), # Ab
    pretty_midi.Note(velocity=100, pitch=47, start=5.25, end=5.4375), # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.4375), # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody in Fm, short motif, make it sing
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.6875), # G
    pretty_midi.Note(velocity=100, pitch=50, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.0625, end=2.25), # E
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.4375), # G
    pretty_midi.Note(velocity=100, pitch=55, start=2.4375, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=2.8125), # G
    pretty_midi.Note(velocity=100, pitch=50, start=2.8125, end=3.0), # Eb

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.1875), # G
    pretty_midi.Note(velocity=100, pitch=50, start=3.1875, end=3.375), # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=100, pitch=51, start=3.5625, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=3.9375), # G
    pretty_midi.Note(velocity=100, pitch=55, start=3.9375, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.3125), # G
    pretty_midi.Note(velocity=100, pitch=50, start=4.3125, end=4.5), # Eb

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.6875), # G
    pretty_midi.Note(velocity=100, pitch=50, start=4.6875, end=4.875), # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=100, pitch=51, start=5.0625, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.4375), # G
    pretty_midi.Note(velocity=100, pitch=55, start=5.4375, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=5.8125), # G
    pretty_midi.Note(velocity=100, pitch=50, start=5.8125, end=6.0), # Eb
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.save("fm_intro.mid")
