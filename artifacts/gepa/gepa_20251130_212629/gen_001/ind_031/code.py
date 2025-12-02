
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
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drum_snare = pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125)
drum_snare2 = pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25)
drum_hihat = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
drum_hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0)

drums.notes.extend([drum_kick, drum_kick2, drum_snare, drum_snare2, drum_hihat, drum_hihat2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=54, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=53, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=54, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=80, pitch=54, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=53, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=51, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Saxophone: simple motif, starts on F, ends on Bb, with a pause in between
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.8125),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    start = bar * 1.5
    kick_start = start
    kick_end = start + 0.375
    kick2_start = start + 1.125
    kick2_end = kick2_start + 0.375
    snare_start = start + 0.75
    snare_end = start + 1.125
    snare2_start = start + 1.875
    snare2_end = snare2_start + 0.375
    hihat_start = start
    hihat_end = start + 1.5
    hihat2_start = start + 1.5
    hihat2_end = start + 3.0

    # Add kick
    drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    drums.notes.append(drum_kick)
    drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=kick2_start, end=kick2_end)
    drums.notes.append(drum_kick2)
    # Add snare
    drum_snare = pretty_midi.Note(velocity=90, pitch=38, start=snare_start, end=snare_end)
    drums.notes.append(drum_snare)
    drum_snare2 = pretty_midi.Note(velocity=90, pitch=38, start=snare2_start, end=snare2_end)
    drums.notes.append(drum_snare2)
    # Add hihat
    drum_hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end)
    drums.notes.append(drum_hihat)
    drum_hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=hihat2_start, end=hihat2_end)
    drums.notes.append(drum_hihat2)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
