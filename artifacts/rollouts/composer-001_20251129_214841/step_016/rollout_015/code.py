
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.75),   # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.75, 0.75),  # Snare on 2
    (42, 0.75, 0.375), # Hihat on 2
    (36, 1.125, 0.75), # Kick on 3
    (42, 1.125, 0.375),# Hihat on 3
    (38, 1.5, 0.75),   # Snare on 4
    (42, 1.5, 0.375)   # Hihat on 4
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line - walking, chromatic approaches, no repeated notes
bass_notes = [
    (60, 1.5, 0.375),  # C
    (61, 1.875, 0.375), # C#
    (62, 2.25, 0.375),  # D
    (63, 2.625, 0.375), # D#
    (64, 3.0, 0.375),   # E
    (65, 3.375, 0.375), # F
    (66, 3.75, 0.375),  # F#
    (67, 4.125, 0.375), # G
    (68, 4.5, 0.375),   # G#
    (69, 4.875, 0.375), # A
    (70, 5.25, 0.375),  # A#
    (71, 5.625, 0.375), # B
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + dur))

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.5, 0.375),  # C
    (64, 1.5, 0.375),  # E
    (67, 1.5, 0.375),  # G
    (71, 1.5, 0.375),  # B
    # Bar 3
    (60, 2.625, 0.375), # C
    (64, 2.625, 0.375), # E
    (67, 2.625, 0.375), # G
    (71, 2.625, 0.375), # B
    # Bar 4
    (60, 3.75, 0.375),  # C
    (64, 3.75, 0.375),  # E
    (67, 3.75, 0.375),  # G
    (71, 3.75, 0.375),  # B
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + dur))

# Sax - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),  # D
    (65, 1.875, 0.375), # F
    (67, 2.25, 0.375),  # G
    (65, 2.625, 0.375), # F
    (62, 3.0, 0.375),   # D
    (64, 3.375, 0.375), # E
    (67, 3.75, 0.375),  # G
    (69, 4.125, 0.375), # A
    (67, 4.5, 0.375),   # G
    (64, 4.875, 0.375), # E
    (62, 5.25, 0.375),  # D
    (60, 5.625, 0.375)  # C
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Drums continue in bars 2-4
drum_notes = [
    (36, 1.5, 0.75),   # Kick on 1
    (42, 1.5, 0.375),  # Hihat on 1
    (38, 1.875, 0.75), # Snare on 2
    (42, 1.875, 0.375),# Hihat on 2
    (36, 2.25, 0.75),  # Kick on 3
    (42, 2.25, 0.375), # Hihat on 3
    (38, 2.625, 0.75), # Snare on 4
    (42, 2.625, 0.375),# Hihat on 4
    (36, 3.0, 0.75),   # Kick on 1
    (42, 3.0, 0.375),  # Hihat on 1
    (38, 3.375, 0.75), # Snare on 2
    (42, 3.375, 0.375),# Hihat on 2
    (36, 3.75, 0.75),  # Kick on 3
    (42, 3.75, 0.375), # Hihat on 3
    (38, 4.125, 0.75), # Snare on 4
    (42, 4.125, 0.375),# Hihat on 4
    (36, 4.5, 0.75),   # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.75), # Snare on 2
    (42, 4.875, 0.375),# Hihat on 2
    (36, 5.25, 0.75),  # Kick on 3
    (42, 5.25, 0.375), # Hihat on 3
    (38, 5.625, 0.75), # Snare on 4
    (42, 5.625, 0.375) # Hihat on 4
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
