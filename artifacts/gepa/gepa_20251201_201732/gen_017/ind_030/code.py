
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

# Add drum notes to the drum instrument
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (Fm), roots and fifths with chromatic approaches
# Fm: F, C, Ab, D, Bb, E, Db, G
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=80, pitch=58, start=1.875, end=2.25), # C (fifth)
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625), # Ab (chromatic)
    pretty_midi.Note(velocity=80, pitch=55, start=2.625, end=3.0),  # D (chromatic)
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # Bb (chromatic)
    pretty_midi.Note(velocity=80, pitch=57, start=3.375, end=3.75), # E (chromatic)
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.125), # Db (chromatic)
    pretty_midi.Note(velocity=80, pitch=56, start=4.125, end=4.5),  # G (chromatic)
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=80, pitch=58, start=4.875, end=5.25), # C (fifth)
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625), # Ab (chromatic)
    pretty_midi.Note(velocity=80, pitch=55, start=5.625, end=6.0),  # D (chromatic)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # D

    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # Ab

    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# You: Tenor sax - one short motif, make it sing
# Start it, leave it hanging, come back and finish it
# Motif: F (Ab) - Bb (C) - D (F) - G (Ab)
# 1.5s - 2.25s: F (Ab)
# 2.25s - 3.0s: Bb (C)
# 3.0s - 3.75s: D (F)
# 4.5s - 5.25s: G (Ab)

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=5.25),  # Ab
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
