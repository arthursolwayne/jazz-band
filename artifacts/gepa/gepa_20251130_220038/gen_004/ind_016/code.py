
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on &
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875), # Hihat on 4
    (42, 1.3125, 0.1875) # Hihat on &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (40, 1.5, 0.375), # F
    (39, 1.875, 0.375), # Eb
    (41, 2.25, 0.375), # Gb
    (42, 2.625, 0.375), # Ab
    (40, 2.625, 0.375), # F
    (41, 3.0, 0.375), # Gb
    (39, 3.375, 0.375), # Eb
    (40, 3.75, 0.375), # F
    (41, 4.125, 0.375), # Gb
    (42, 4.5, 0.375), # Ab
    (43, 4.875, 0.375), # Bb
    (42, 5.25, 0.375), # Ab
    (43, 5.625, 0.375), # Bb
    (42, 6.0, 0.375) # Ab
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comping on 2 and 4
piano_notes = [
    # Bar 2
    (48, 1.875, 0.375), # F7 - F
    (50, 1.875, 0.375), # F7 - A
    (52, 1.875, 0.375), # F7 - C
    (53, 1.875, 0.375), # F7 - Eb
    # Bar 3
    (52, 3.0, 0.375), # F7 - C
    (54, 3.0, 0.375), # F7 - E
    (56, 3.0, 0.375), # F7 - G
    (57, 3.0, 0.375), # F7 - Ab
    # Bar 4
    (48, 4.5, 0.375), # F7 - F
    (50, 4.5, 0.375), # F7 - A
    (52, 4.5, 0.375), # F7 - C
    (53, 4.5, 0.375), # F7 - Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody - short motif, start it, leave it hanging, come back
sax_notes = [
    # Bar 2
    (50, 1.5, 0.375), # Gb
    (52, 1.875, 0.375), # Ab
    (50, 2.25, 0.375), # Gb
    # Bar 3
    (53, 2.625, 0.375), # Bb
    (50, 3.0, 0.375), # Gb
    (52, 3.375, 0.375), # Ab
    # Bar 4
    (50, 3.75, 0.375), # Gb
    (52, 4.125, 0.375), # Ab
    (50, 4.5, 0.375), # Gb
    (52, 4.875, 0.375), # Ab
    (50, 5.25, 0.375), # Gb
    (52, 5.625, 0.375), # Ab
    (50, 6.0, 0.375) # Gb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("f_minor_intro.mid")
