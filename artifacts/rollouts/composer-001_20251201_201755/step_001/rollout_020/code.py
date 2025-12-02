
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
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Dm7 -> Gm7 -> C7 -> F7 (no modulation)
sax_notes = [
    (62, 1.5), (65, 1.75), (67, 2.0), (65, 2.25),  # Dm7
    (67, 2.5), (70, 2.75), (72, 3.0), (70, 3.25),  # Gm7
    (72, 3.5), (74, 3.75), (76, 4.0), (74, 4.25),  # C7
    (76, 4.5), (79, 4.75), (81, 5.0), (79, 5.25)   # F7
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    (50, 1.5), (49, 1.75), (50, 2.0), (52, 2.25),  # D -> C# -> D -> F
    (52, 2.5), (51, 2.75), (52, 3.0), (54, 3.25),  # F -> E -> F -> A
    (54, 3.5), (53, 3.75), (54, 4.0), (56, 4.25),  # A -> G -> A -> C
    (56, 4.5), (55, 4.75), (56, 5.0), (58, 5.25)   # C -> B -> C -> E
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    (62, 1.5), (65, 1.5), (67, 1.5), (70, 1.5),
    # Bar 3: Gm7 (G Bb D F)
    (67, 2.5), (71, 2.5), (69, 2.5), (70, 2.5),
    # Bar 4: C7 (C E G Bb)
    (60, 3.5), (64, 3.5), (67, 3.5), (71, 3.5)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 1.0)
    piano.notes.append(n)

# Drums: Fill the bar
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    drum_notes = [
        (36, bar_start), (38, bar_start + 0.375), (42, bar_start + 0.375),
        (36, bar_start + 0.75), (38, bar_start + 1.125), (42, bar_start + 1.125),
        (36, bar_start + 1.5), (38, bar_start + 1.875), (42, bar_start + 1.875)
    ]
    for note, time in drum_notes:
        dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
        drums.notes.append(dr)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
