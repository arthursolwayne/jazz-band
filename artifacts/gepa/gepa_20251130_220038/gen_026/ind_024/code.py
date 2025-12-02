
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
#ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375), # Kick on 1
    (42, 0.0, 0.375), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375), # Kick on 3
    (42, 0.75, 0.375), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, Dm7
bass_notes = [
    (62, 1.5, 0.375), # D
    (63, 1.875, 0.375), # Eb (chromatic approach)
    (60, 2.25, 0.375), # C
    (62, 2.625, 0.375), # D
    (65, 3.0, 0.375), # F
    (63, 3.375, 0.375), # Eb
    (60, 3.75, 0.375), # C
    (62, 4.125, 0.375), # D
    (67, 4.5, 0.375), # G
    (65, 4.875, 0.375), # F
    (63, 5.25, 0.375), # Eb
    (62, 5.625, 0.375) # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 1.5, 0.375), # F7 (root)
    (67, 1.5, 0.375), # 3rd
    (69, 1.5, 0.375), # 5th
    (71, 1.5, 0.375), # 7th
    (67, 1.875, 0.375), # 3rd
    (69, 1.875, 0.375), # 5th
    (71, 1.875, 0.375), # 7th
    (64, 2.25, 0.375), # F7 (root)
    (67, 2.25, 0.375), # 3rd
    (69, 2.25, 0.375), # 5th
    (71, 2.25, 0.375), # 7th
    (67, 2.625, 0.375), # 3rd
    (69, 2.625, 0.375), # 5th
    (71, 2.625, 0.375), # 7th
    (64, 3.0, 0.375), # F7 (root)
    (67, 3.0, 0.375), # 3rd
    (69, 3.0, 0.375), # 5th
    (71, 3.0, 0.375), # 7th
    (67, 3.375, 0.375), # 3rd
    (69, 3.375, 0.375), # 5th
    (71, 3.375, 0.375), # 7th
    (64, 3.75, 0.375), # F7 (root)
    (67, 3.75, 0.375), # 3rd
    (69, 3.75, 0.375), # 5th
    (71, 3.75, 0.375), # 7th
    (67, 4.125, 0.375), # 3rd
    (69, 4.125, 0.375), # 5th
    (71, 4.125, 0.375), # 7th
    (64, 4.5, 0.375), # F7 (root)
    (67, 4.5, 0.375), # 3rd
    (69, 4.5, 0.375), # 5th
    (71, 4.5, 0.375), # 7th
    (67, 4.875, 0.375), # 3rd
    (69, 4.875, 0.375), # 5th
    (71, 4.875, 0.375), # 7th
    (64, 5.25, 0.375), # F7 (root)
    (67, 5.25, 0.375), # 3rd
    (69, 5.25, 0.375), # 5th
    (71, 5.25, 0.375), # 7th
    (67, 5.625, 0.375), # 3rd
    (69, 5.625, 0.375), # 5th
    (71, 5.625, 0.375) # 7th
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.25), # D
    (64, 1.75, 0.25), # F
    (65, 2.0, 0.25), # G
    (64, 2.25, 0.25), # F (reprise)
    (62, 2.5, 0.25), # D (reprise)
    (64, 2.75, 0.25), # F (reprise)
    (65, 3.0, 0.25), # G (reprise)
    (64, 3.25, 0.25), # F (reprise)
    (62, 3.5, 0.25), # D (reprise)
    (64, 3.75, 0.25), # F (reprise)
    (65, 4.0, 0.25), # G (reprise)
    (64, 4.25, 0.25), # F (reprise)
    (62, 4.5, 0.25), # D (reprise)
    (64, 4.75, 0.25), # F (reprise)
    (65, 5.0, 0.25), # G (reprise)
    (64, 5.25, 0.25), # F (reprise)
    (62, 5.5, 0.25), # D (reprise)
    (64, 5.75, 0.25) # F (reprise)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375), # Kick on 1
    (42, 1.5, 0.375), # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.375), # Hihat on 2
    (36, 2.25, 0.375), # Kick on 3
    (42, 2.25, 0.375), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.375), # Hihat on 4
    # Bar 3
    (36, 3.0, 0.375), # Kick on 1
    (42, 3.0, 0.375), # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.375), # Hihat on 2
    (36, 3.75, 0.375), # Kick on 3
    (42, 3.75, 0.375), # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.375), # Hihat on 4
    # Bar 4
    (36, 4.5, 0.375), # Kick on 1
    (42, 4.5, 0.375), # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.375), # Hihat on 2
    (36, 5.25, 0.375), # Kick on 3
    (42, 5.25, 0.375), # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
