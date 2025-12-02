
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
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice. He's the anchor.
bass_notes = [
    (64, 1.5, 0.375),  # F (root)
    (65, 1.875, 0.375), # Gb (chromatic approach)
    (65, 2.25, 0.375),  # Gb (chromatic)
    (64, 2.625, 0.375), # F
    (63, 3.0, 0.375),   # E (up a half step)
    (62, 3.375, 0.375), # D
    (63, 3.75, 0.375),  # D (up a half step)
    (64, 4.125, 0.375), # E
    (65, 4.5, 0.375),   # F
    (66, 4.875, 0.375), # F# (chromatic)
    (66, 5.25, 0.375),  # F#
    (65, 5.625, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4. Stay out of your way but keep it moving.
piano_notes = [
    (64, 1.5, 0.125),  # F7 (F, A, C, Eb) on 1
    (69, 1.5, 0.125),  # A
    (60, 1.5, 0.125),  # C
    (62, 1.5, 0.125),  # Eb
    (66, 1.875, 0.125), # F# (chromatic passing)
    (69, 1.875, 0.125), # A
    (60, 1.875, 0.125), # C
    (62, 1.875, 0.125), # Eb
    (64, 2.25, 0.125),  # F7 on 3
    (69, 2.25, 0.125),  # A
    (60, 2.25, 0.125),  # C
    (62, 2.25, 0.125),  # Eb
    (66, 2.625, 0.125), # F#
    (69, 2.625, 0.125), # A
    (60, 2.625, 0.125), # C
    (62, 2.625, 0.125), # Eb
    (64, 3.0, 0.125),   # F7 on 1
    (69, 3.0, 0.125),   # A
    (60, 3.0, 0.125),   # C
    (62, 3.0, 0.125),   # Eb
    (66, 3.375, 0.125), # F#
    (69, 3.375, 0.125), # A
    (60, 3.375, 0.125), # C
    (62, 3.375, 0.125), # Eb
    (64, 3.75, 0.125),  # F7 on 3
    (69, 3.75, 0.125),  # A
    (60, 3.75, 0.125),  # C
    (62, 3.75, 0.125),  # Eb
    (66, 4.125, 0.125), # F#
    (69, 4.125, 0.125), # A
    (60, 4.125, 0.125), # C
    (62, 4.125, 0.125), # Eb
    (64, 4.5, 0.125),   # F7 on 1
    (69, 4.5, 0.125),   # A
    (60, 4.5, 0.125),   # C
    (62, 4.5, 0.125),   # Eb
    (66, 4.875, 0.125), # F#
    (69, 4.875, 0.125), # A
    (60, 4.875, 0.125), # C
    (62, 4.875, 0.125), # Eb
    (64, 5.25, 0.125),  # F7 on 3
    (69, 5.25, 0.125),  # A
    (60, 5.25, 0.125),  # C
    (62, 5.25, 0.125),  # Eb
    (66, 5.625, 0.125), # F#
    (69, 5.625, 0.125), # A
    (60, 5.625, 0.125), # C
    (62, 5.625, 0.125)  # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# You: This is your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs — that's student shit.
sax_notes = [
    (66, 1.5, 0.375),  # F#
    (69, 1.875, 0.375), # A
    (66, 2.25, 0.375),  # F#
    (69, 2.625, 0.375), # A
    (66, 3.0, 0.375),   # F#
    (69, 3.375, 0.375), # A
    (66, 3.75, 0.375),  # F#
    (69, 4.125, 0.375), # A
    (66, 4.5, 0.375),   # F#
    (69, 4.875, 0.375), # A
    (66, 5.25, 0.375),  # F#
    (69, 5.625, 0.375)  # A
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Add the drums for bars 2-4
drum_notes = [
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.5, 0.375),   # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.375), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.375), # Hihat on 4
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.375),   # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.375), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.375), # Hihat on 4
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.375),   # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.375), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
