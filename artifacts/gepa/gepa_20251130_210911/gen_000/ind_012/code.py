
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (48, 1.5), (49, 1.875), (47, 2.25), (46, 2.625),
    # Bar 3
    (45, 3.0), (44, 3.375), (43, 3.75), (42, 4.125),
    # Bar 4
    (41, 4.5), (40, 4.875), (42, 5.25), (43, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 1, Bb7 on beat 3
    (53, 1.5), (60, 1.5), (64, 1.5), (67, 1.5),  # Fm7
    (62, 2.25), (67, 2.25), (71, 2.25), (74, 2.25),  # Bb7
    # Bar 3: Fm7 on beat 1, Bb7 on beat 3
    (53, 3.0), (60, 3.0), (64, 3.0), (67, 3.0),  # Fm7
    (62, 3.75), (67, 3.75), (71, 3.75), (74, 3.75),  # Bb7
    # Bar 4: Fm7 on beat 1, Bb7 on beat 3
    (53, 4.5), (60, 4.5), (64, 4.5), (67, 4.5),  # Fm7
    (62, 5.25), (67, 5.25), (71, 5.25), (74, 5.25)   # Bb7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (53), Ab (55), G (54), F (53) — but with a twist (chromatic approach)
sax_notes = [
    (53, 1.5), (55, 1.875), (54, 2.25), (53, 2.625),  # First phrase (bar 2)
    (53, 3.0), (55, 3.375), (54, 3.75), (53, 4.125),  # Second phrase (bar 3)
    (53, 4.5), (55, 4.875), (54, 5.25), (53, 5.625)   # Third phrase (bar 4)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.125))

# Drums: Continue the pattern for bars 2-4
for bar in range(2, 5):
    start_time = 1.5 + bar * 1.5
    drum_notes = [
        (36, start_time), (38, start_time + 0.375), (42, start_time + 0.375),
        (36, start_time + 0.75), (38, start_time + 1.125), (42, start_time + 1.125),
        (36, start_time + 1.5), (38, start_time + 1.875), (42, start_time + 1.875)
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
