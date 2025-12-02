
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (24, 1.5, 0.375), (25, 1.875, 0.375), (23, 2.25, 0.375), (22, 2.625, 0.375),
    (24, 3.0, 0.375), (25, 3.375, 0.375), (23, 3.75, 0.375), (22, 4.125, 0.375),
    (24, 4.5, 0.375), (25, 4.875, 0.375), (23, 5.25, 0.375), (22, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Fm7 on 1.875, Bb7 on 3.375, Eb7 on 4.875
chords = [
    # Fm7 (F, Ab, C, Eb)
    (53, 1.875, 0.375), (60, 1.875, 0.375), (64, 1.875, 0.375), (65, 1.875, 0.375),
    # Bb7 (Bb, D, F, Ab)
    (57, 3.375, 0.375), (62, 3.375, 0.375), (53, 3.375, 0.375), (60, 3.375, 0.375),
    # Eb7 (Eb, G, Bb, D)
    (65, 4.875, 0.375), (67, 4.875, 0.375), (57, 4.875, 0.375), (62, 4.875, 0.375)
]
for note, start, duration in chords:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Motif in Fm. Start with a short line, leave it hanging, return to finish
# Fm: F, Ab, Bb, C, Eb
sax_notes = [
    (53, 1.5, 0.375), (60, 1.875, 0.375), (57, 2.25, 0.375),  # F -> Ab -> Bb
    (64, 3.0, 0.375), (65, 3.375, 0.375), (53, 3.75, 0.375),  # C -> Eb -> F
    (60, 4.5, 0.375), (57, 4.875, 0.375)  # Ab -> Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Continue pattern for bars 2-4
for bar in range(2, 4):
    start_time = 1.5 + (bar - 2) * 1.5
    for i in range(4):
        kick_start = start_time + i * 0.75
        snare_start = kick_start + 0.375
        hihat_start = start_time + i * 0.75
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375))
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375))
        for j in range(2):
            hihat_start_sub = hihat_start + j * 0.375
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start_sub, end=hihat_start_sub + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
