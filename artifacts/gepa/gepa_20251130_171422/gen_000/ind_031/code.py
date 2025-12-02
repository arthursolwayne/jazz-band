
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
for bar in range(1):
    start = bar * 1.5
    # Kick on beat 0 and 2
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 1 and 3
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# Fm7 = F Ab C Eb
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),  # Db
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25), # Db
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=63, start=5.625, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F Ab C Eb
# Bb7 = Bb D F Ab
# Cm7 = C Eb G Bb
# Eb7 = Eb G Bb D
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Ab
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Ab
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Bb
    # Bar 4 (second half)
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
]
piano.notes.extend(piano_notes)

# Drums: continue same pattern for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on beat 0 and 2
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 1 and 3
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F, Ab, A, Bb (descending 3rd, then ascending)
# Play first two notes on beat 1 and 2, leave the rest hanging for now
note1 = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.8125)
note4 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.1875)
sax.notes.extend([note1, note2, note3, note4])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
