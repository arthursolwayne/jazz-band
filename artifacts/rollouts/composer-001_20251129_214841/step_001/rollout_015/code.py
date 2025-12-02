
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (36, 1.125, 0.375),# Kick on 3
    (38, 1.5, 0.375),  # Snare on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line with chromatic approaches
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
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.5, 0.375),  # C
    (64, 1.5, 0.375),  # E
    (67, 1.5, 0.375),  # G
    (71, 1.5, 0.375),  # B
    (64, 2.25, 0.375), # E
    (67, 2.25, 0.375), # G
    (71, 2.25, 0.375), # B
    (74, 2.25, 0.375), # D
    # Bar 3
    (60, 3.0, 0.375),  # C
    (64, 3.0, 0.375),  # E
    (67, 3.0, 0.375),  # G
    (71, 3.0, 0.375),  # B
    (64, 3.75, 0.375), # E
    (67, 3.75, 0.375), # G
    (71, 3.75, 0.375), # B
    (74, 3.75, 0.375), # D
    # Bar 4
    (60, 4.5, 0.375),  # C
    (64, 4.5, 0.375),  # E
    (67, 4.5, 0.375),  # G
    (71, 4.5, 0.375),  # B
    (64, 5.25, 0.375), # E
    (67, 5.25, 0.375), # G
    (71, 5.25, 0.375), # B
    (74, 5.25, 0.375), # D
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    for i in [0, 2]:
        kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375)
        drums.notes.append(kick)
    # Snare on 2 and 4
    for i in [1, 3]:
        snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375)
        drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375)
        drums.notes.append(hihat)

# Sax: Motif in C minor, with a question and a wait
sax_notes = [
    (60, 1.5, 0.375),  # C
    (62, 1.875, 0.375), # D
    (60, 2.25, 0.375),  # C
    (59, 2.625, 0.375), # Bb
    (60, 3.0, 0.375),   # C
    (62, 3.375, 0.375), # D
    (63, 3.75, 0.375),  # D#
    (62, 4.125, 0.375), # D
    (60, 4.5, 0.375),   # C
    (62, 4.875, 0.375), # D
    (60, 5.25, 0.375),  # C
    (59, 5.625, 0.375), # Bb
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
