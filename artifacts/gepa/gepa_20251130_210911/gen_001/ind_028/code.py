
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4 (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0), # E

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=80, pitch=66, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5), # D

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=61, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=63, start=5.625, end=6.0), # Eb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # F#
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # C

    # Bar 3 - G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # B
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # F

    # Bar 4 - C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # B
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante) - melody in D, one short motif, sing it
sax_notes = [
    # Bar 2 - motif starts
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0), # E
    pretty_midi.Note(velocity=110, pitch=63, start=2.0, end=2.25), # C
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5), # D

    # Bar 3 - motif continues
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25), # C
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5), # D
    pretty_midi.Note(velocity=110, pitch=66, start=3.5, end=3.75), # E
    pretty_midi.Note(velocity=110, pitch=63, start=3.75, end=4.0), # C

    # Bar 4 - motif finishes
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75), # D
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0), # E
    pretty_midi.Note(velocity=110, pitch=63, start=5.0, end=5.25), # C
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5), # D
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75), # F#
    pretty_midi.Note(velocity=110, pitch=65, start=5.75, end=6.0), # F
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4 (Little Ray)
drum_notes_bars2_4 = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.0), # Hihat

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.5), # Hihat

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.0), # Hihat
]

for note in drum_notes_bars2_4:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
