
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
kick_notes = [36, 36, 36, 36]
snare_notes = [38, 38, 38, 38]
hihat_notes = [42] * 8

for i in range(4):
    kick_time = 0.0 + i * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=kick_notes[i], start=kick_time, end=kick_time + 0.375)
    drums.notes.append(kick)

for i in range(4):
    snare_time = 0.75 + i * 1.5
    snare = pretty_midi.Note(velocity=100, pitch=snare_notes[i], start=snare_time, end=snare_time + 0.375)
    drums.notes.append(snare)

for i in range(8):
    hihat_time = i * 0.375
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.1875)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line, chromatic approaches
bass_notes = [
    53, 52, 51, 50,  # Bar 2
    49, 48, 47, 51,  # Bar 3
    52, 53, 51, 50,  # Bar 4
    51, 52, 53, 51   # Bar 4
]
for i, note in enumerate(bass_notes):
    time = 1.5 + (i * 0.375)
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: Diane, 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    53, 60, 64, 61,
    # Bar 3: Bb7 (Bb, D, F, Ab)
    58, 62, 53, 60,
    # Bar 4: Eb7 (Eb, G, Bb, Db)
    61, 67, 58, 59
]
for i, note in enumerate(piano_notes):
    time = 1.5 + (i * 0.375)
    if i % 2 == 1:  # Play on 2 and 4
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
        piano.notes.append(piano_note)

# Sax: Dante, short motif
# Fm scale: F, Gb, Ab, A, Bb, B, C
sax_notes = [53, 60, 64, 61, 53, 60, 64, 61]  # F, Gb, Ab, A, F, Gb, Ab, A
for i, note in enumerate(sax_notes):
    time = 1.5 + (i * 0.375)
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("fm_intro.mid")
