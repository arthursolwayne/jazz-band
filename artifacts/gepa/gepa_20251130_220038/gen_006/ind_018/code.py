
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.1875),  # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875),# Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),  # D (root)
    (63, 1.875, 0.375), # Eb (chromatic approach)
    (60, 2.25, 0.375),  # Bb (3rd)
    (61, 2.625, 0.375), # B (chromatic)
    (65, 3.0, 0.375),   # F (5th)
    (66, 3.375, 0.375), # F# (chromatic)
    (62, 3.75, 0.375),  # D (root)
    (63, 4.125, 0.375), # Eb (chromatic)
    (60, 4.5, 0.375),   # Bb (3rd)
    (61, 4.875, 0.375), # B (chromatic)
    (65, 5.25, 0.375),  # F (5th)
    (66, 5.625, 0.375)  # F# (chromatic)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.5, 0.375),  # D7 - D
    (67, 1.5, 0.375),  # D7 - F#
    (69, 1.5, 0.375),  # D7 - A
    (71, 1.5, 0.375),  # D7 - C
    # Bar 3
    (62, 2.625, 0.375), # D7 - D
    (67, 2.625, 0.375), # D7 - F#
    (69, 2.625, 0.375), # D7 - A
    (71, 2.625, 0.375), # D7 - C
    # Bar 4
    (62, 3.75, 0.375),  # D7 - D
    (67, 3.75, 0.375),  # D7 - F#
    (69, 3.75, 0.375),  # D7 - A
    (71, 3.75, 0.375),  # D7 - C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: Melody - one short motif, make it sing
sax_notes = [
    # Bar 2
    (62, 1.5, 0.375),  # D
    (64, 1.875, 0.375), # E
    (62, 2.25, 0.375),  # D
    (60, 2.625, 0.375), # Bb
    # Bar 3
    (62, 3.0, 0.375),  # D
    (64, 3.375, 0.375), # E
    (62, 3.75, 0.375),  # D
    (60, 4.125, 0.375), # Bb
    # Bar 4
    (62, 4.5, 0.375),  # D
    (64, 4.875, 0.375), # E
    (62, 5.25, 0.375),  # D
    (60, 5.625, 0.375)  # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    for i in [0, 2]:
        kick_start = start + i * 0.75
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375))
    # Snare on 2 and 4
    for i in [1, 3]:
        snare_start = start + i * 0.75
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375))
    # Hihat on every eighth
    for i in range(8):
        hihat_start = start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
