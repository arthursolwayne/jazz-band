
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
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.75, 0.375),
    (36, 1.125, 0.375), (38, 1.5, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking in D, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (65, 2.25, 0.375), (67, 2.625, 0.375),
    (69, 3.0, 0.375), (71, 3.375, 0.375), (72, 3.75, 0.375), (74, 4.125, 0.375),
    (76, 4.5, 0.375), (77, 4.875, 0.375), (79, 5.25, 0.375), (81, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: comping on 2 and 4 with 7th chords
piano_notes = [
    (74, 2.25, 0.125), (76, 2.25, 0.125), (72, 2.25, 0.125), (69, 2.25, 0.125), # D7
    (74, 3.75, 0.125), (76, 3.75, 0.125), (72, 3.75, 0.125), (69, 3.75, 0.125), # D7
    (74, 5.25, 0.125), (76, 5.25, 0.125), (72, 5.25, 0.125), (69, 5.25, 0.125)  # D7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = 1.5 + (bar - 2) * 1.5
    drum_notes = [
        (36, start, 0.375), (38, start + 0.375, 0.375), (42, start + 0.75, 0.375),
        (36, start + 1.125, 0.375), (38, start + 1.5, 0.375)
    ]
    for note, s, d in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d))

# Sax: motif in D, one phrase, start it, leave it hanging
# Motif: D - F# - B - E (inspired by Coltrane, but not a run)
sax_notes = [
    (62, 1.5, 0.375), (66, 1.875, 0.375), (67, 2.25, 0.375), (69, 2.625, 0.375),
    (62, 3.0, 0.375), (66, 3.375, 0.375), (67, 3.75, 0.375), (69, 4.125, 0.375),
    (62, 4.5, 0.375), (66, 4.875, 0.375), (67, 5.25, 0.375), (69, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_shorter_intro.mid")
