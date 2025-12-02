
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=37, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=35, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=34, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=33, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=32, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=31, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=30, start=4.125, end=4.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=37, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=35, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=34, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # F7 (Ab)
    pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=1.875),  # F7 (C)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F7 (F)
    pretty_midi.Note(velocity=100, pitch=39, start=1.5, end=1.875),  # F7 (Gb)
    pretty_midi.Note(velocity=100, pitch=44, start=2.25, end=2.625),  # F7 (Ab)
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625),  # F7 (C)
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),  # F7 (F)
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625),  # F7 (Gb)
    pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.125),  # F7 (Ab)
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125),  # F7 (C)
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # F7 (F)
    pretty_midi.Note(velocity=100, pitch=39, start=3.75, end=4.125),  # F7 (Gb)
    pretty_midi.Note(velocity=100, pitch=44, start=5.25, end=5.625),  # F7 (Ab)
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625),  # F7 (C)
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # F7 (F)
    pretty_midi.Note(velocity=100, pitch=39, start=5.25, end=5.625),  # F7 (Gb)
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = 1.5 + (bar - 2) * 1.5
    kick_start = start
    kick_end = kick_start + 0.375
    snare_start = start + 0.75
    snare_end = snare_start + 0.375
    hihat_start = start
    hihat_end = hihat_start + 0.375
    hihat_start2 = hihat_start + 0.75
    hihat_end2 = hihat_start2 + 0.375
    hihat_start3 = hihat_start + 1.5
    hihat_end3 = hihat_start3 + 0.375
    hihat_start4 = hihat_start + 2.25
    hihat_end4 = hihat_start4 + 0.375

    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end),  # Snare on 2
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125),  # Kick on 3
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875),  # Snare on 4
        pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end),  # Hihat on 1
        pretty_midi.Note(velocity=100, pitch=42, start=hihat_start2, end=hihat_end2),  # Hihat on 2
        pretty_midi.Note(velocity=100, pitch=42, start=hihat_start3, end=hihat_end3),  # Hihat on 3
        pretty_midi.Note(velocity=100, pitch=42, start=hihat_start4, end=hihat_end4),  # Hihat on 4
    ]
    drums.notes.extend(drum_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.75),  # D7
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F7
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # C7
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.5),  # D7
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # F7
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # C7
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.75),  # D7
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # F7
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # C7
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.5),  # D7
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # F7
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # C7
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
