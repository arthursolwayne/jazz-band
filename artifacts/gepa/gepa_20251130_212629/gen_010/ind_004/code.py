
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
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42), (1.5, 36),
    (1.875, 42), (2.25, 38), (2.625, 42), (3.0, 36)
]

for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm, chromatic approaches, no repeated notes
# Fm: F, Ab, Bb, D, Eb, G, Ab
# Walking bass line in Fm (1.5 - 6.0s)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 64), (1.875, 63), (2.25, 62), (2.625, 61),
    # Bar 3 (3.0 - 4.5s)
    (3.0, 60), (3.375, 59), (3.75, 58), (4.125, 57),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 56), (4.875, 55), (5.25, 54), (5.625, 53)
]

for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Diane: 7th chords, comp on 2 and 4 (1.5 - 6.0s)
# Fm7 = F, Ab, Bb, D
# Bb7 = Bb, D, F, Ab
# Ab7 = Ab, B, Db, E
# Eb7 = Eb, G, Bb, Db
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 64), (1.5, 76), (1.5, 71), (1.5, 69),  # Fm7
    (2.25, 64), (2.25, 76), (2.25, 71), (2.25, 69),  # Fm7
    # Bar 3 (3.0 - 4.5s)
    (3.0, 71), (3.0, 76), (3.0, 74), (3.0, 72),  # Bb7
    (3.75, 71), (3.75, 76), (3.75, 74), (3.75, 72),  # Bb7
    # Bar 4 (4.5 - 6.0s)
    (4.5, 69), (4.5, 81), (4.5, 79), (4.5, 77),  # Ab7
    (5.25, 69), (5.25, 81), (5.25, 79), (5.25, 77),  # Ab7
]

for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Dante: Tenor sax motif. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, rest, return with F, Ab, Bb, rest
sax_notes = [
    (1.5, 82), (1.875, 89), (2.25, 87), (2.625, 82),  # First pass
    (3.0, 82), (3.375, 89), (3.75, 87), (4.125, 82),  # Second pass
    (4.5, 82), (4.875, 89), (5.25, 87), (5.625, 82)   # Third pass
]

for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# Drums continue for bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 + (bar - 2) * 1.5
    drum_notes = [
        (bar_start, 36), (bar_start + 0.375, 42), (bar_start + 0.75, 38), (bar_start + 1.125, 42),
        (bar_start + 1.5, 36), (bar_start + 1.875, 42), (bar_start + 2.25, 38), (bar_start + 2.625, 42)
    ]
    for time, note in drum_notes:
        drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
        drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
