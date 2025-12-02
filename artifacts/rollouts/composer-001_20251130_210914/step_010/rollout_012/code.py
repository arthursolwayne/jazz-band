
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
kick_time = 0.0
snare_time = 0.75
hihat_time = 0.0
for i in range(4):
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.375)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.1875)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat)
    kick_time += 1.5
    snare_time += 1.5
    hihat_time += 0.375

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=49, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # D7: D, F, A, C
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # D7: same
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # D7: same
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Sax: short motif, start on beat 1, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # D
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
kick_time = 1.5
snare_time = 2.25
hihat_time = 1.5
for i in range(3):
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.375)
    for j in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.1875)
        drums.notes.append(hihat)
        hihat_time += 0.375
    drums.notes.append(kick)
    drums.notes.append(snare)
    kick_time += 1.5
    snare_time += 1.5

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
