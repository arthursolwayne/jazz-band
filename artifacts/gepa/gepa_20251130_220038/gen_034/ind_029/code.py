
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
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.append(kick1)
    drums.notes.append(kick2)
    drums.notes.append(snare1)
    drums.notes.append(snare2)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
# F minor walking bass line (F, Gb, G, A, Bb, B, C, Db, etc.)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),  # A

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=75, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),  # Db

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0),  # A
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# F7, Bb7, E7, A7
# Bar 2: F7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=82, start=2.25, end=2.625), # A

    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=81, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=84, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=87, start=3.375, end=3.75), # A

    # Bar 4: E7 on beat 2
    pretty_midi.Note(velocity=90, pitch=79, start=4.375, end=4.75), # E
    pretty_midi.Note(velocity=90, pitch=84, start=4.375, end=4.75), # G
    pretty_midi.Note(velocity=90, pitch=87, start=4.375, end=4.75), # B
    pretty_midi.Note(velocity=90, pitch=90, start=4.375, end=4.75), # D

    # Bar 4: A7 on beat 4
    pretty_midi.Note(velocity=90, pitch=82, start=5.625, end=6.0), # A
    pretty_midi.Note(velocity=90, pitch=87, start=5.625, end=6.0), # C
    pretty_midi.Note(velocity=90, pitch=90, start=5.625, end=6.0), # E
    pretty_midi.Note(velocity=90, pitch=93, start=5.625, end=6.0), # G
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F Gb A F (motif) - then leave it hanging on Gb, then come back with F A Gb F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=100, pitch=70, start=1.6875, end=1.875), # Gb
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.0625), # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.0625, end=2.25), # F

    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625), # Gb (left hanging)
    
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.1875), # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.1875, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.5625), # Gb
    pretty_midi.Note(velocity=100, pitch=71, start=3.5625, end=3.75), # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: continue for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on beat 0 and 2
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 1 and 3
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.append(kick1)
    drums.notes.append(kick2)
    drums.notes.append(snare1)
    drums.notes.append(snare2)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
