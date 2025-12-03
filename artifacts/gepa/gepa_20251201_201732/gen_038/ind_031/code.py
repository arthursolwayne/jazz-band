
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
bar1_start = 0.0
bar1_end = 1.5
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.0, end=bar1_start + 0.1),
              pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.375 * 2, end=bar1_start + 0.375 * 2 + 0.1)]
snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.375, end=bar1_start + 0.375 + 0.1),
               pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.375 * 3, end=bar1_start + 0.375 * 3 + 0.1)]
hihat_notes = [pretty_midi.Note(velocity=100, pitch=42, start=bar1_start + i * 0.375, end=bar1_start + i * 0.375 + 0.05)
               for i in range(4)]
drums.notes.extend(kick_notes + snare_notes + hihat_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches, not scales
bar2_start = 1.5
bar2_end = 3.0
bar3_start = 3.0
bar3_end = 4.5
bar4_start = 4.5
bar4_end = 6.0

# Dm7 chord: D, F, A, C (MIDI 43, 46, 49, 52)
# G7 chord: G, B, D, F (MIDI 47, 50, 52, 55)
# Cm7 chord: C, Eb, G, Bb (MIDI 52, 55, 59, 60)

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4
piano_notes = []
# Bar 2: Dm7 (MIDI 49, 52, 56, 59)
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=49, start=bar2_start, end=bar2_end),
                    pretty_midi.Note(velocity=100, pitch=52, start=bar2_start, end=bar2_end),
                    pretty_midi.Note(velocity=100, pitch=56, start=bar2_start, end=bar2_end),
                    pretty_midi.Note(velocity=100, pitch=59, start=bar2_start, end=bar2_end)])
# Bar 3: G7 (MIDI 52, 55, 57, 60)
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=52, start=bar3_start, end=bar3_end),
                    pretty_midi.Note(velocity=100, pitch=55, start=bar3_start, end=bar3_end),
                    pretty_midi.Note(velocity=100, pitch=57, start=bar3_start, end=bar3_end),
                    pretty_midi.Note(velocity=100, pitch=60, start=bar3_start, end=bar3_end)])
# Bar 4: Cm7 (MIDI 52, 55, 59, 60)
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=52, start=bar4_start, end=bar4_end),
                    pretty_midi.Note(velocity=100, pitch=55, start=bar4_start, end=bar4_end),
                    pretty_midi.Note(velocity=100, pitch=59, start=bar4_start, end=bar4_end),
                    pretty_midi.Note(velocity=100, pitch=60, start=bar4_start, end=bar4_end)])
piano.notes.extend(piano_notes)

# Marcus: Walking bass line in Dm
# Bar 2: D, F, G, C
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=46, start=bar2_start + 0.375, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=47, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=52, start=bar2_start + 1.125, end=bar2_end),
    # Bar 3: G, Bb, A, D
    pretty_midi.Note(velocity=100, pitch=47, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=50, start=bar3_start + 0.375, end=bar3_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=49, start=bar3_start + 0.75, end=bar3_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=52, start=bar3_start + 1.125, end=bar3_end),
    # Bar 4: C, Eb, D, G
    pretty_midi.Note(velocity=100, pitch=52, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=55, start=bar4_start + 0.375, end=bar4_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=52, start=bar4_start + 0.75, end=bar4_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=57, start=bar4_start + 1.125, end=bar4_end)
]
bass.notes.extend(bass_notes)

# You: Tenor sax motif – start it, leave it hanging, come back and finish it
# Melody: D (43), F (46), E (45), D (43) in bar 2
# Then on bar 3: G (47), Bb (50), A (49), G (47)
# Then on bar 4: C (52), Eb (55), D (52), C (52)

# Bar 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=46, start=bar2_start + 0.375, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=45, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=43, start=bar2_start + 1.125, end=bar2_end)
]
# Bar 3
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=47, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=50, start=bar3_start + 0.375, end=bar3_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=49, start=bar3_start + 0.75, end=bar3_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=47, start=bar3_start + 1.125, end=bar3_end)
])
# Bar 4
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=52, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=55, start=bar4_start + 0.375, end=bar4_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=52, start=bar4_start + 0.75, end=bar4_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=52, start=bar4_start + 1.125, end=bar4_end)
])
sax.notes.extend(sax_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
for bar_start in [bar2_start, bar3_start, bar4_start]:
    kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.0, end=bar_start + 0.1),
                  pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.375 * 2, end=bar_start + 0.375 * 2 + 0.1)]
    snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.375 + 0.1),
                   pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375 * 3, end=bar_start + 0.375 * 3 + 0.1)]
    hihat_notes = [pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.05)
                   for i in range(4)]
    drums.notes.extend(kick_notes + snare_notes + hihat_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
