
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(name='C3', start=start, end=start + 0.375, velocity=100, instrument=drums)
    pretty_midi.Note(name='C3', start=start + 0.75, end=start + 1.125, velocity=100, instrument=drums)
    # Snare
    pretty_midi.Note(name='C3', start=start + 0.375, end=start + 0.75, velocity=110, instrument=drums)
    pretty_midi.Note(name='C3', start=start + 1.125, end=start + 1.5, velocity=110, instrument=drums)
    # Hi-hat
    pretty_midi.Note(name='C3', start=start, end=start + 0.375, velocity=90, instrument=drums)
    pretty_midi.Note(name='C3', start=start + 0.375, end=start + 0.75, velocity=90, instrument=drums)
    pretty_midi.Note(name='C3', start=start + 0.75, end=start + 1.125, velocity=90, instrument=drums)
    pretty_midi.Note(name='C3', start=start + 1.125, end=start + 1.5, velocity=90, instrument=drums)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# Dm7 chord: D F A C
# Walking bass line in D minor
bass_notes = [
    # Bar 2
    ('C#2', 1.5), ('D2', 1.875), ('E2', 2.25), ('F2', 2.625),
    # Bar 3
    ('F#2', 2.625), ('G2', 3.0), ('A2', 3.375), ('Bb2', 3.75),
    # Bar 4
    ('B2', 3.75), ('C2', 4.125), ('C#2', 4.5), ('D2', 4.875),
]

for note, start in bass_notes:
    pretty_midi.Note(name=note, start=start, end=start + 0.375, velocity=90, instrument=bass)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Comp on beat 2 and 4
piano_notes = [
    # Bar 2
    ('F2', 1.875, 0.375), ('A2', 1.875, 0.375), ('C3', 1.875, 0.375),
    ('F2', 2.625, 0.375), ('A2', 2.625, 0.375), ('C3', 2.625, 0.375),
    # Bar 3
    ('F2', 3.0, 0.375), ('A2', 3.0, 0.375), ('C3', 3.0, 0.375),
    ('F2', 3.75, 0.375), ('A2', 3.75, 0.375), ('C3', 3.75, 0.375),
    # Bar 4
    ('F2', 4.125, 0.375), ('A2', 4.125, 0.375), ('C3', 4.125, 0.375),
    ('F2', 4.875, 0.375), ('A2', 4.875, 0.375), ('C3', 4.875, 0.375),
]

for note, start, duration in piano_notes:
    pretty_midi.Note(name=note, start=start, end=start + duration, velocity=90, instrument=piano)

# Drums: same as bar 1, repeated
for bar in range(2, 4):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(name='C3', start=start, end=start + 0.375, velocity=100, instrument=drums)
    pretty_midi.Note(name='C3', start=start + 0.75, end=start + 1.125, velocity=100, instrument=drums)
    # Snare
    pretty_midi.Note(name='C3', start=start + 0.375, end=start + 0.75, velocity=110, instrument=drums)
    pretty_midi.Note(name='C3', start=start + 1.125, end=start + 1.5, velocity=110, instrument=drums)
    # Hi-hat
    pretty_midi.Note(name='C3', start=start, end=start + 0.375, velocity=90, instrument=drums)
    pretty_midi.Note(name='C3', start=start + 0.375, end=start + 0.75, velocity=90, instrument=drums)
    pretty_midi.Note(name='C3', start=start + 0.75, end=start + 1.125, velocity=90, instrument=drums)
    pretty_midi.Note(name='C3', start=start + 1.125, end=start + 1.5, velocity=90, instrument=drums)

# Sax: One short motif, make it sing
# Dm scale: D, Eb, F, G, Ab, Bb, C
# Motif: D, Eb, F, D (sings, leaves it hanging)
sax_notes = [
    ('D4', 1.5, 0.375),
    ('Eb4', 1.875, 0.375),
    ('F4', 2.25, 0.375),
    ('D4', 2.625, 0.375),
    # Repeat the motif
    ('D4', 3.0, 0.375),
    ('Eb4', 3.375, 0.375),
    ('F4', 3.75, 0.375),
    ('D4', 4.125, 0.375),
]

for note, start, duration in sax_notes:
    pretty_midi.Note(name=note, start=start, end=start + duration, velocity=105, instrument=sax)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
