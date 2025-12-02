
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
    (36, 0.0, 0.375), (42, 0.0, 0.125),
    (38, 0.375, 0.375), (42, 0.375, 0.125),
    (36, 0.75, 0.375), (42, 0.75, 0.125),
    (38, 1.125, 0.375), (42, 1.125, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (34, 1.5, 0.375), # Fm root
    (35, 1.875, 0.375), # b9
    (33, 2.25, 0.375), # 7
    (32, 2.625, 0.375), # b7
    (34, 2.999, 0.375), # Fm root
    (36, 3.375, 0.375), # 9
    (35, 3.75, 0.375), # b9
    (34, 4.125, 0.375), # root
    (33, 4.5, 0.375), # 7
    (32, 4.875, 0.375), # b7
    (34, 5.25, 0.375), # root
    (35, 5.625, 0.375), # b9
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (47, 1.5, 0.375), (50, 1.5, 0.375), (52, 1.5, 0.375), (55, 1.5, 0.375), # F7
    # Bar 3
    (47, 3.0, 0.375), (50, 3.0, 0.375), (52, 3.0, 0.375), (55, 3.0, 0.375), # F7
    # Bar 4
    (47, 4.5, 0.375), (50, 4.5, 0.375), (52, 4.5, 0.375), (55, 4.5, 0.375), # F7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.125)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.5)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.875)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.25)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.375, end=start + 1.5)
    
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4, hihat5])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm (F, Ab, C, Eb)
sax_notes = [
    (53, 1.5, 0.375),  # F
    (50, 1.875, 0.375), # Ab
    (55, 2.25, 0.375),  # C
    (52, 2.625, 0.375), # Eb
    # Leave it hanging
    (55, 2.999, 0.001), # C (short)
    # Come back and finish it
    (53, 3.0, 0.375),  # F
    (50, 3.375, 0.375), # Ab
    (55, 3.75, 0.375),  # C
    (52, 4.125, 0.375), # Eb
    (53, 4.5, 0.375),   # F
    (50, 4.875, 0.375), # Ab
    (55, 5.25, 0.375),  # C
    (52, 5.625, 0.375)  # Eb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
