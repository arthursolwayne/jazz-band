
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (36, 1.125, 0.375),
    (38, 1.5, 0.375), (42, 1.5, 0.1875),
]

for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# D minor scale: D, Eb, F, G, Ab, Bb, C
# Walking line in D minor
bass_notes = [
    # Bar 2
    (62, 1.5, 0.375), (61, 1.875, 0.375), (64, 2.25, 0.375), (63, 2.625, 0.375),
    # Bar 3
    (67, 3.0, 0.375), (66, 3.375, 0.375), (65, 3.75, 0.375), (62, 4.125, 0.375),
    # Bar 4
    (64, 4.5, 0.375), (63, 4.875, 0.375), (62, 5.25, 0.375), (61, 5.625, 0.375)
]

for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
# D7 chord: D, F#, A, C
# Dm7 chord: D, F, Ab, Bb
piano_notes = [
    # Bar 2
    (62, 1.875, 0.375), (67, 1.875, 0.375), (69, 1.875, 0.375), (67, 1.875, 0.375),
    (62, 2.625, 0.375), (67, 2.625, 0.375), (69, 2.625, 0.375), (67, 2.625, 0.375),
    # Bar 3
    (62, 3.375, 0.375), (66, 3.375, 0.375), (67, 3.375, 0.375), (65, 3.375, 0.375),
    (62, 4.125, 0.375), (66, 4.125, 0.375), (67, 4.125, 0.375), (65, 4.125, 0.375),
    # Bar 4
    (62, 4.875, 0.375), (67, 4.875, 0.375), (69, 4.875, 0.375), (67, 4.875, 0.375),
]

for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Sax: Melody - one short motif, start it, leave it hanging. Come back and finish it.
# D minor motif: D, Eb, F, G
sax_notes = [
    # Bar 2
    (62, 1.5, 0.5),  # D
    (64, 2.0, 0.625),  # F
    (69, 2.625, 0.375),  # G
    # Bar 3
    (62, 3.0, 0.5),  # D
    (64, 3.5, 0.625),  # F
    (69, 4.125, 0.375),  # G
    # Bar 4
    (62, 4.5, 0.75)  # D
]

for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)

    drums.notes.append(kick1)
    drums.notes.append(kick3)
    drums.notes.append(snare2)
    drums.notes.append(snare4)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
