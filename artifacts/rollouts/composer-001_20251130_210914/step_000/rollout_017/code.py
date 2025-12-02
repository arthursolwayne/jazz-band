
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.5)

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.875)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 1.875, end=bar1_start + 2.0)

# Hi-hat on every eighth
hihat_notes = [bar1_start + i * 0.375 for i in range(4)]
for hihat_start in hihat_notes:
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.125)
    drums.notes.append(hihat)

drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches, no repeated notes
bass_line = [
    (1.5, 59),    # D (root)
    (1.875, 60),  # Eb (chromatic)
    (2.25, 62),   # F (3rd)
    (2.625, 63),  # Gb (chromatic)
    (3.0, 65),    # G (5th)
    (3.375, 66),  # Ab (chromatic)
    (3.75, 69),   # Bb (7th)
    (4.125, 71),  # B (chromatic)
    (4.5, 69),    # Bb (7th)
    (4.875, 67),  # A (chromatic)
    (5.25, 65),   # G (5th)
    (5.625, 64),  # Gb (chromatic)
    (6.0, 62),    # F (3rd)
]

for start, pitch in bass_line:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 2 and 4
    (2.25, 62),  # F
    (2.25, 64),  # Gb
    (2.25, 67),  # A
    (2.25, 69),  # Bb
    # Bar 3: Dm7 on 2 and 4
    (3.75, 62),
    (3.75, 64),
    (3.75, 67),
    (3.75, 69),
    # Bar 4: Dm7 on 2 and 4
    (5.25, 62),
    (5.25, 64),
    (5.25, 67),
    (5.25, 69),
]

for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125)
    piano.notes.append(note)

# Saxophone: One short motif, make it sing
# Start on Bb (62), then Eb (64), then D (62), leave it hanging on the 4th beat
sax_notes = [
    (1.5, 62),  # Bb
    (1.875, 64),  # Eb
    (2.25, 62),  # D
    (2.625, 62),  # D, held
    (3.0, 62),   # D, held
    (3.375, 62), # D, held
    (3.75, 62),  # D, held
    (4.125, 62), # D, held
    (4.5, 62),   # D, held
    (4.875, 62), # D, held
    (5.25, 62),  # D, held
    (5.625, 62), # D, held
    (6.0, 62),   # D, held
]

for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

# Drums in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 2
bar2_start = 1.5
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar2_start, end=bar2_start + 0.375)
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=bar2_start + 1.125, end=bar2_start + 1.5)

snare3 = pretty_midi.Note(velocity=110, pitch=38, start=bar2_start + 0.75, end=bar2_start + 0.875)
snare4 = pretty_midi.Note(velocity=110, pitch=38, start=bar2_start + 1.875, end=bar2_start + 2.0)

hihat_notes = [bar2_start + i * 0.375 for i in range(4)]
for hihat_start in hihat_notes:
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.125)
    drums.notes.append(hihat)

# Bar 3
bar3_start = 3.0
kick5 = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375)
kick6 = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start + 1.125, end=bar3_start + 1.5)

snare5 = pretty_midi.Note(velocity=110, pitch=38, start=bar3_start + 0.75, end=bar3_start + 0.875)
snare6 = pretty_midi.Note(velocity=110, pitch=38, start=bar3_start + 1.875, end=bar3_start + 2.0)

hihat_notes = [bar3_start + i * 0.375 for i in range(4)]
for hihat_start in hihat_notes:
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.125)
    drums.notes.append(hihat)

# Bar 4
bar4_start = 4.5
kick7 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375)
kick8 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start + 1.125, end=bar4_start + 1.5)

snare7 = pretty_midi.Note(velocity=110, pitch=38, start=bar4_start + 0.75, end=bar4_start + 0.875)
snare8 = pretty_midi.Note(velocity=110, pitch=38, start=bar4_start + 1.875, end=bar4_start + 2.0)

hihat_notes = [bar4_start + i * 0.375 for i in range(4)]
for hihat_start in hihat_notes:
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.125)
    drums.notes.append(hihat)

drums.notes.extend([kick3, kick4, snare3, snare4, kick5, kick6, snare5, snare6, kick7, kick8, snare7, snare8])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
