
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
    (42, 1.125, 0.375), # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line in Fm (F2, G2, Ab2, A2, Bb2, B2, C2, Db2)
bass_notes = [
    (71, 1.5, 0.375),   # F2 on 1
    (72, 1.875, 0.375),  # G2 on 2
    (70, 2.25, 0.375),   # Ab2 on 3
    (71, 2.625, 0.375),  # F2 on 4
    (76, 2.625, 0.375),  # chromatic approach
    (72, 3.0, 0.375),    # G2 on 1
    (74, 3.375, 0.375),  # A2 on 2
    (75, 3.75, 0.375),   # Bb2 on 3
    (76, 4.125, 0.375),  # B2 on 4
    (77, 4.125, 0.375),  # chromatic approach
    (74, 4.5, 0.375),    # A2 on 1
    (77, 4.875, 0.375),  # B2 on 2
    (79, 5.25, 0.375),   # C2 on 3
    (80, 5.625, 0.375),  # Db2 on 4
    (79, 5.625, 0.375),  # chromatic approach
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: Diane, open voicings, different chord each bar, resolve on last
# Bar 2: Fm7
piano_notes = [
    (52, 1.5, 0.375),  # F
    (57, 1.5, 0.375),  # Bb
    (62, 1.5, 0.375),  # F (octave)
    (64, 1.5, 0.375),  # Ab
    (57, 1.5, 0.375),  # Bb (double)
    (68, 1.5, 0.375),  # D
    (69, 1.5, 0.375),  # Eb

    # Bar 3: Gm7
    (55, 2.25, 0.375),  # G
    (60, 2.25, 0.375),  # D
    (65, 2.25, 0.375),  # G (octave)
    (67, 2.25, 0.375),  # Bb
    (60, 2.25, 0.375),  # D (double)
    (72, 2.25, 0.375),  # F
    (73, 2.25, 0.375),  # F#

    # Bar 4: Ab7
    (56, 3.0, 0.375),  # Ab
    (61, 3.0, 0.375),  # Eb
    (66, 3.0, 0.375),  # Ab (octave)
    (68, 3.0, 0.375),  # B
    (61, 3.0, 0.375),  # Eb (double)
    (74, 3.0, 0.375),  # G
    (75, 3.0, 0.375),  # G#
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - G - Bb
sax_notes = [
    (71, 1.5, 0.375),  # F
    (76, 1.875, 0.375), # Bb
    (74, 2.25, 0.375),  # G
    (76, 2.625, 0.375), # Bb
    (71, 3.0, 0.375),   # F
    (76, 3.375, 0.375), # Bb
    (74, 3.75, 0.375),  # G
    (76, 4.125, 0.375), # Bb
    (71, 4.5, 0.375),   # F
    (76, 4.875, 0.375), # Bb
    (74, 5.25, 0.375),  # G
    (76, 5.625, 0.375), # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Bar 2
    if bar == 2:
        kick = 36
        snare = 38
        hihat = 42
        # Kick on 1
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=start, end=start + 0.375))
        # Hihat on 1
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=start, end=start + 0.375))
        # Snare on 2
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=start + 0.375, end=start + 0.375 + 0.375))
        # Hihat on 2
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=start + 0.375, end=start + 0.375 + 0.375))
        # Kick on 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=start + 0.75, end=start + 0.75 + 0.375))
        # Hihat on 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=start + 0.75, end=start + 0.75 + 0.375))
        # Snare on 4
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=start + 1.125, end=start + 1.125 + 0.375))
        # Hihat on 4
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=start + 1.125, end=start + 1.125 + 0.375))
    # Bars 3 and 4
    else:
        kick = 36
        snare = 38
        hihat = 42
        # Kick on 1
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=start, end=start + 0.375))
        # Hihat on 1
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=start, end=start + 0.375))
        # Snare on 2
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=start + 0.375, end=start + 0.375 + 0.375))
        # Hihat on 2
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=start + 0.375, end=start + 0.375 + 0.375))
        # Kick on 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=start + 0.75, end=start + 0.75 + 0.375))
        # Hihat on 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=start + 0.75, end=start + 0.75 + 0.375))
        # Snare on 4
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=start + 1.125, end=start + 1.125 + 0.375))
        # Hihat on 4
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=start + 1.125, end=start + 1.125 + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
